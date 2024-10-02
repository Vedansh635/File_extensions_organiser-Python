# Project-Description

This program organizes all the files in a given folder into subfolders based on their file extension. For example, if the folder contains files with `.txt`, `.pdf`, and `.docx` extensions, the program will create three subfolders: `txt` `files`, `pdf` files, and `docx` files, and move the files accordingly.

# How it works

1. The program loops through all the files in the given folder.<br>
2. For each file, it checks if it's a file (not a folder).<br>
3. It gets the file extension and creates a new folder for this extension if it doesn't exist.<br>
4. The file is then moved to the new folder.<br>

# Usage

1. Simply input the path to the folder that needs to be organized.
2. The program will take care of the rest, creating subfolders and moving files as needed.
   
# Features

- Organizes files by extension
- Creates subfolders for each file type
- Moves files to their corresponding subfolders
- Easy to use: just input the folder path
  
# Requirements

- Python 3.x
- `pathlib` and `shutil` modules (included in Python standard library)
