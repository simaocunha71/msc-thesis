def count_char_position(s):
    s = s.lower()
    count = 0
    for i in range(len(s)):
        if ord(s[i]) - 96 == i + 1:
            count += 1
    return count