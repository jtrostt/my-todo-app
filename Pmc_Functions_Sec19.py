import sys
print(sys.version)
print("Python Mega Course - Section19_Functions")

def get_todos(filepath="todos.txt"):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath="todos.txt"):
    """ Write the to-do items list in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

print(__name__)
if __name__ == "__main__":
    print("NEIL SEZ - hello")
    print(get_todos())