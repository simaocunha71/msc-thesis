def count_char_position(s):
    count = 0
    for i in range(len(s)):
        if s[i].lower() == chr(96 + i):
            count += 1
    return count