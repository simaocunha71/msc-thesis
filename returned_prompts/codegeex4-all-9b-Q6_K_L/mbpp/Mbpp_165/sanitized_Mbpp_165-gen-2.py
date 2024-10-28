def count_char_position(s):
    count = 0
    for i, c in enumerate(s):
        if c.lower() == chr(ord('a') + i):
            count += 1
    return count