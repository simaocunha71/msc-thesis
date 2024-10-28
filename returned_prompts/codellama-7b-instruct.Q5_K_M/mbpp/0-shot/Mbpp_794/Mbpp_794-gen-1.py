"""
import re

def text_starta_endb(my_string):
    return re.match(r"a.+b$", my_string)

# Tests
assert text_starta_endb("aabbbb")
assert not text_starta_endb("abb")
assert not text_starta_endb("aab")
"""

