def get_read_todos(filepath="todos.txt"):
    """ Read a text file and return the list
    of to-do items. """
    with open(filepath, 'r') as file_local:  # best way to handle files
        todos_local = file_local.readlines()
    return todos_local


def get_write_todos(todos_arg, filepath="todos.txt"):
    """ Write the to-do items list in the next file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__todo_app_using_if_else__":
    print("Hello")
    print(get_read_todos())