"""
def count_char_position(s):
    c = 0
    for i in range(26):
        for ch in s:
            if ch.lower() == chr(97+i):
                c += 1
    return c
"""
