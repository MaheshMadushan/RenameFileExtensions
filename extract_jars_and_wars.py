import os
from pathlib import Path

def extract_jars_and_wars(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            extract_jars_and_wars(os.path.join(dirpath, dirname))

        for filename in filenames:
            original_file = Path(os.path.join(dirpath, filename))
            if original_file.suffix == ".jar" or original_file.suffix == ".war":
                os.system(f"jar xf {original_file}")
                print(f"Extracting Jar File '{original_file}'")

extract_jars_and_wars(os.getcwd())
