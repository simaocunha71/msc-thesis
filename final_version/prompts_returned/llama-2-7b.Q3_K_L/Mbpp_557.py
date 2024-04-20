"""
Write a function to toggle the case of all characters in a string.
assert toggle_string("Python")==("pYTHON")
"""
from typing import Optional, List

def toggle(s: str):
	if len(s) == 0: return s # empty strings should be lowercase.
	return [x[::-1] if x in ('A', 'a') else x for x in s][::-1]
