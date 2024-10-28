def count_char_position(s):
    s = s.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    for i in range(len(s)):
        if s[i] in alphabet and alphabet.index(s[i]) == i:
            count += 1
    return count