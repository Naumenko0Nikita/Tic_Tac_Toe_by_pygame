import os

def find_path_to_file(name_file):
    path_file = __file__.split("\\")
    del path_file [-1]
    del path_file [-1]
    path_file = "\\".join(path_file)
    path_file = os.path.join(path_file, name_file)
    print(find_path_to_file)
    return path_file