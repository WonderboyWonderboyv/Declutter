# Declutter
#a python program to organise your PC files
# Declutter
  - scan C:/User/* (Windows) and /home/* (Linux) recursively and identifies the top 10 files which have the largest size on the system.
  - sort the files on Desktop on the basis of file extension and move them in
separate folders in Documents folder.

It uses the function of OS module of python 3 such as os.path, os.walk to traverse through all the folders recursively and storing the size of each file encountered.
The size of each file is then sorted and printed.
The desktop files are scanned and based on their extensions they are sorted into their respective folders and files are copied from the desktop to the destination folder using the function shutil.copy2 and lastly deleting that file from the desktop.
