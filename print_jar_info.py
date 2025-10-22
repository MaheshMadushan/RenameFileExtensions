import os
from pathlib import Path



def print_jar_info(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            print_jar_info(os.path.join(dirpath, dirname))

        for filename in filenames:
            original_file = Path(os.path.join(dirpath, filename))
            if original_file.suffix == ".class":
                os.system("javap -v {original_file}")
                print(f"Extracting Jar File '{original_file}'")
print_jar_info(os.getcwd())
