def find_char_long(s):
    return [word for word in s.split() if len(word) >= 4]

assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])


"""
