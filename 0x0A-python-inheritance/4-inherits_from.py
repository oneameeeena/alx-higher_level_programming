#!/usr/bin/python3
'''Module for is_true_subclass method.'''

from typing import Type, Any

def is_true_subclass(obj: Any, a_class: Type) -> bool:
    '''Determines if an object is a true subclass of a class.

    A true subclass is a subclass that is not the same as the class itself.
    This is important to distinguish because some methods, such as isinstance(),
    will return True for both the class and its subclasses.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is a true subclass of a_class, False otherwise.
    '''
    return isinstance(obj, a_class) and type(obj) != a_class
