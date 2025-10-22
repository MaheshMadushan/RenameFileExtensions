import os
from pathlib import Path
import subprocess

def find_class_file_version(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            find_class_file_version(os.path.join(dirpath, dirname))

        for filename in filenames:
            original_file = Path(os.path.join(dirpath, filename))
            if original_file.suffix == ".class":
                p = subprocess.Popen(f"javap -v {original_file} | findStr \"major\"", stdout=subprocess.PIPE, shell=True)
                out, err = p.communicate()
                print("loading")
                class_file_version = out.decode('utf-8')
                if (not err):
                    if class_file_version.strip() == "53":
                        print(f"class version of class File '{original_file}' = {class_file_version.strip()}")
                else:
                    print(err)
find_class_file_version(os.getcwd())
