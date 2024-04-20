#!/usr/bin/python3
"""Define function write_file"""



def write_file(filename="", text=""):
    """
    Write a string to a UTF-8 encoded text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    
    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)

