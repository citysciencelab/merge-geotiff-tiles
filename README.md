# Merge tiles in subdirectories
* test `pip --version` and `python --version` in `cmd.exe` or `powershell.exe` to make sure that Python and PIP are installed. Python version must be `>=3.7`
* if PIP is not available using the `pip` command in the terminal, open `install.bat` and replace `pip` with the absolute path to PIP like `"/Path/To/Pip.exe"`
* if Python is not available using the `python` command in the terminal, open `merge.bat` and replace `python` with the absolute path to PIP like `"/Path/To/Python3.exe"`, or the `python3` command respectively.
* Run `install.bat` (by double-clicking) to install necessary libraries.
* Run `run.bat` to scan and merge all relative subdirectories
    * you can test this using the provided test files in `altona` and `eimsbuettel`, delete or move them before merging the real tiles.
* Relative path to scan and output folder name can be changed inside `merge.py`
* All output and errpr logs will be written to `log.txt`
* You can also run the python script directly from command line, using
```
python merge.py > log.txt
```