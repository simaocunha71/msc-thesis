"""
Write a function that matches a string that has an 'a' followed by anything, ending in 'b'.
assert text_starta_endb("aabbbb")
"""
from typing import Any, List

def text_starta_endb(text: str):
	"""Write a function that matches a string that has an 'a' followed by anything, ending in 'b'.
    assert text_starta_endb("aabbbb")
    """
	s = text.lower()
	if s[0] == "a":
		return True if s[-1] == "b" else False
	else: return False

# Write a function that matches a string that has an 'a' followed by anything, ending in 'b'.
assert text_starta_endb("aabbbb")

