def count_char_position(s):
    s = s.lower()
    count = 0
    for i, c in enumerate(s):
        if c == chr(ord('a') + i):
            count += 1
    return count