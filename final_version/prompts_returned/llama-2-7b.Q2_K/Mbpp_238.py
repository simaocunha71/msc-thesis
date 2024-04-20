"""
Write a python function to count the number of non-empty substrings of a given string.
assert number_of_substrings("abc") == 6
"""
import re

def number_of_substrings(s):
    def recursive_visit(current, visited):
        if current[0] not in visited and len(str(current)) > 1:
            visited.add(str(current)[0])
            recursive_visit([current[1:] for _ in range(1, len(s))], visited)
    return int(recursive_visit([str(i) for i in s] , set()) or 0)
