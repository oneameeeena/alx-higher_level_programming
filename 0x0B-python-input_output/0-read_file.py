#!/usr/bin/python3



"""Define a function read_file"""
def read_file(filename=""):
    """Read and print the contents of a file."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

