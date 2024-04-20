"""
Write a function to find all words which are at least 4 characters long in a string.
assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])
"""
import re
def find_char_long(s):
    res = [] # set()
    for i in s:
        if len(i)>=4 and i not in ['.','?']:
            res.add(i)
    return res
