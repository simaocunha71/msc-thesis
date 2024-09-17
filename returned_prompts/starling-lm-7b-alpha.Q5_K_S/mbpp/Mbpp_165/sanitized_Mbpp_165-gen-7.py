def count_char_position(s):
    res = 0
    for i, c in enumerate(s):
        if ord(c.lower()) == i + 97:
            res += 1
    return res