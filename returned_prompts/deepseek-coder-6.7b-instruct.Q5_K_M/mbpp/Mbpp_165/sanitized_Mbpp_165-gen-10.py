def count_char_position(s):
    count = 0
    s = s.lower()
    for i in range(len(s)):
        if s[i] == chr(97+i):
            count += 1
    return count