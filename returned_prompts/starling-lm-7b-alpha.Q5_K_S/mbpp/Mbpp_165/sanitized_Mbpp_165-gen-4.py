def count_char_position(s):
    count = 0
    for c, i in zip(s.lower(), range(len(s))):
        if ord(c) - i == ord('a'):
            count += 1
    return count