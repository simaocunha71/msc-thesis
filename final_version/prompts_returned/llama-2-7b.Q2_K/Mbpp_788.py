"""
Write a function to create a new tuple from the given string and list.
assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
"""

def new_tuple(string, *list):
    if isinstance(string,(str, unicode)):
        return tuple((string,) + list)  # str to (str, ...)
    else:
        return tuple([string] + list)   # [str] -> [(str, )+...]
