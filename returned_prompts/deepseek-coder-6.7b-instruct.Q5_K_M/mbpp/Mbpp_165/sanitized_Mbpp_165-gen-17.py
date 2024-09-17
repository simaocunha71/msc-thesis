def count_char_position(s):
    return sum(1 for c, l in zip(s.lower(), 'abcdefghijklmnopqrstuvwxyz') if c == l)