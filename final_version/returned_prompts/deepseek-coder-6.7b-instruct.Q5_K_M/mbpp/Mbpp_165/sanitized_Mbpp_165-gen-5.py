def count_char_position(s):
    return sum(1 for c1, c2 in zip(s.lower(), 'abcdefghijklmnopqrstuvwxyz') if c1 == c2)