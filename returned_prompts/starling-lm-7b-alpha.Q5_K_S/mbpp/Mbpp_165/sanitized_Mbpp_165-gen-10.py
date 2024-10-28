def count_char_position(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    for i, c in enumerate(s):
        if c.lower() == alphabet[i]:
            count += 1
    return count