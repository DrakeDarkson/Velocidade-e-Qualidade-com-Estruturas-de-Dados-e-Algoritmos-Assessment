import os

def list_files_recursive(directory):
    for entry in os.scandir(directory):
        if entry.is_file():
            print(f"File: {entry.path}")
        elif entry.is_dir():
            list_files_recursive(entry.path)

directory_path = "C:/Users/breno/Pictures"
list_files_recursive(directory_path)
