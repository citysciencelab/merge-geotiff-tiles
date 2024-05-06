import os
import shutil
import rasterio
from rasterio.merge import merge

# CHANGE IF NECESSARY
OUT_DIR_NAME = "fhh_gesamt"
BASE_DIRECTORY = "./"


merged_tiles = []
merged_tiles_count = 0

# prepare output dir
out_dir_path = os.path.join(BASE_DIRECTORY, OUT_DIR_NAME)
if os.path.isdir(out_dir_path):
    print(f"removing old {out_dir_path}")
    shutil.rmtree(out_dir_path)
os.mkdir(out_dir_path)

# iterate through sub directories
for path, folders, files in os.walk(BASE_DIRECTORY):
    for folder_name in folders:
        _path = os.path.join(BASE_DIRECTORY, folder_name)
        print(f"iterating over tiles in {_path}")
        for tile in [f_name for f_name in os.listdir(_path) if (".tiff" in f_name or ".tif" in f_name) and f_name not in merged_tiles]:
            tile_path = os.path.join(_path, tile)
            src = rasterio.open(tile_path)
            src_files = [src]
            out_path = os.path.join(out_dir_path, tile)
            for other_folder in [d for d in folders if d != folder_name]:
                print(f"comparing {tile_path} to files in {other_folder}")
                other_path = os.path.join(BASE_DIRECTORY, other_folder)
                matching_tile = next((f_name for f_name in os.listdir(other_path) if f_name == tile), None)
                if matching_tile:
                    print(f"found matching {matching_tile}")
                    matching_tile_path = os.path.join(other_path, matching_tile)
                    print(matching_tile_path)
                    src_files.append(rasterio.open(matching_tile_path))
            if len(src_files) > 0:
                print(f"found {len(src_files)} matching tiles, merging ...")
                merged, out_trans = merge(src_files)
                out_meta = src.meta.copy()
                out_meta.update({
                    "driver": "GTiff",
                    "height": merged.shape[1],
                    "width": merged.shape[2],
                    "transform": out_trans 
                })
                with rasterio.open(out_path, "w", **out_meta) as dest:
                    dest.write(merged)
                    print(f"written merged {out_path}")
            else:
                print(f"no matching tile for {tile_path}, copying original ...")
                shutil.copyfile(tile_path, out_path)
            merged_tiles.append(tile)
            merged_tiles_count += 1
    break

print(f"processed tiles: {merged_tiles_count}")