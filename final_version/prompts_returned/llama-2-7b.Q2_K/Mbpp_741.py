"""
Write a python function to check whether all the characters are same or not.
assert all_Characters_Same("python") == False
"""
from typing import Optional, List

def all_Characters_Same(s:str) ->bool:
    if s is None:return True
    if type(s) is not str:
        return False
    for char in s:
        if ord(char) > 255:break
    else: return False
    return ord(s[0]) == ord(s[-1])
