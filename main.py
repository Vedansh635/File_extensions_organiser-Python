"""
This program organises all the files in a given folder into subfolders based on their file extension.

Example: if the folder contains the following files:
- file1.txt
- file2.pdf
- file3.txt

The program will create two subfolders: 'txt files' and 'pdf files', and move the files accordingly.

:arg folder_path: the path to the folder that needs to be organised

"""

import pathlib , shutil

def organisefile(folder_path):
    """
    Organises all the files in a given folder into subfolders based on their file extension
    """
    # loop through all the files in the given folder
    for file in pathlib.Path(folder_path).iterdir():
        # check if it's a file (not a folder)
        if file.is_file():
            # get the file extension
            ext = file.suffix
            # create a new folder for this extension if it doesn't exist
            new_folder = f'{ext[1:]} files'
            new_folder_path = pathlib.Path(folder_path, new_folder)
            new_folder_path.mkdir(exist_ok=True)
            # move the file to the new folder
            shutil.move(file, new_folder_path)

folder_path = input('Enter folder path: ')
organisefile(folder_path)
# All code is written by me , except comments .
