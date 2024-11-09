import pathlib
import shutil

def organisefile(folder_path):
    """
    Organises all the files in a given folder into subfolders based on their file extension.
    """
    # Loop through all the files in the given folder
    for file in pathlib.Path(folder_path).iterdir():
        # Check if it's a file (not a folder)
        if file.is_file():
            # Get the file extension
            ext = file.suffix
            # Create a new folder for this extension if it doesn't exist
            new_folder = f'{ext[1:]} files'
            new_folder_path = pathlib.Path(folder_path, new_folder)
            new_folder_path.mkdir(exist_ok=True)
            
            # Define the destination path for the file
            destination = new_folder_path / file.name
            
            # Check if a file with the same name exists at the destination
            if destination.exists():
                # Generate a new name if a file with the same name already exists
                base = destination.stem
                count = 1
                while destination.exists():
                    # Create a new file name with a count appended
                    destination = new_folder_path / f"{base}_{count}{file.suffix}"
                    count += 1
            
            # Move the file to the new folder with the final unique name
            shutil.move(file, destination)

folder_path = input("Enter the path of the folder: ")
organisefile(folder_path)
