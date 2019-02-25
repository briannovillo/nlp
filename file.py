import os

def read_file(FILENAME):
    with open(FILENAME, 'rb') as f:
        file = f.read()
    return file

def delete_file(FILENAME):
    return os.remove(FILENAME)

def execute_cmd(COMMAND):
    os.system(COMMAND)
