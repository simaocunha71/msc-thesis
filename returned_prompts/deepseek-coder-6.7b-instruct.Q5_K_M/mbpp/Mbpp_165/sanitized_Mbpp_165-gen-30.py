def count_char_position(s):
    return sum(1 for c, a in zip(s.lower(), 'abcdefghijklmnopqrstuvwxyz') if c == a)