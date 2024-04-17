#!/usr/bin/python3
"""Defines a function, is_same_class"""


def is_same_class(obj, a_class):
    """checks if is exactly an instance of a specified class."""
    return type(obj) == a_class
