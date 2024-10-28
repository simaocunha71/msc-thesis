def count_char_position(s):
    count = 0
    for i, c in enumerate(s.lower()):
        if c == chr(ord('a') + i):
            count += 1
    return count