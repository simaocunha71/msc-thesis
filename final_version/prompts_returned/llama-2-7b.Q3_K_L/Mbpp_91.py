"""
Write a function to check if a string is present as a substring in a given list of string values.
assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
"""
from typing import List, Tuple

def find_substring(strlist:List[Tuple[str, str]], substring: str) -> bool:
    substring = [s for s in strlist if substring in s]
    return len(substring) > 0