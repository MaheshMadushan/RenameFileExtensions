import os
from pathlib import Path

def walk_directory_recursive(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        print(f"Directory: {dirpath}")

        for dirname in dirnames:
            print(f"  Subdirectory: {os.path.join(dirpath, dirname)}")
            walk_directory_recursive(os.path.join(dirpath, dirname))

        for filename in filenames:
            original_file = Path(os.path.join(dirpath, filename))

            new_extension = ".java"

            print(original_file.suffix)

            if original_file.suffix == ".class":

                new_file = original_file.with_suffix(new_extension)

                original_file.rename(new_file)

                print(f"File '{original_file}' renamed to '{new_file}'")

walk_directory_recursive(os.getcwd())
