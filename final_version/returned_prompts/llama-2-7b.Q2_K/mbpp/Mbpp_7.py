"""
Write a function to find all words which are at least 4 characters long in a string.
assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])
"""
def find_character_long(string):
    return [i for i, x in enumerate(string) if len(x[0]) > 3]