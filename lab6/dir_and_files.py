#exercise 1:
import os

def list_dir_files(path):
    items = os.listdir(path)
    dirs = [item for item in items if os.path.isdir(os.path.join(path, item))]
    files = [item for item in items if os.path.isfile(os.path.join(path, item))]

    print("Directories:", dirs)
    print("Files:", files)
    print("All items:", items)

#exercise 2:
import os
def check_access(path):
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

#exercise 3:
import os
def test_path_details(path):
    if os.path.exists(path):
        print("Path exists.")
        print("Directory:", os.path.dirname(path))
        print("Filename:", os.path.basename(path))
    else:
        print("Path does not exist.")

#exercise 4:
import os

def count_lines(file_path):
    with open(file_path, 'r') as file:
        print("Number of lines:", len(file.readlines()))

#exercise 5:
import os

def write_list_to_file(list_items, file_path):
    with open(file_path, 'w') as file:
        for item in list_items:
            file.write(f"{item}\n")

#exercise 6:
import os

def generate_26_files():
    for i in range(65, 91): 
        with open(f"{chr(i)}.txt", 'w') as file:
            file.write(chr(i))

#exercise 7:
import os

def copy_file(source_path, destination_path):
    with open(source_path, 'r') as source, open(destination_path, 'w') as dest:
        dest.write(source.read())

#exercise 8:
import os
def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        print("File deleted.")
    else:
        print("File does not exist or is not accessible.")