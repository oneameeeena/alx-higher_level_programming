#!/usr/bin/python3

def append_write(filename="", text=""):
    """
    Append a string to a UTF-8 encoded text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.
    
    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
