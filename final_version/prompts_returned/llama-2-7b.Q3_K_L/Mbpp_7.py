"""
Write a function to find all words which are at least 4 characters long in a string.
assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])
"""
from typing import List, Set

def find_char_long(string: str):
    words = []
    for i in string.split():
        words += i[1:]
    
    return list(set(words))

if __name__ == '__main__':
    assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])