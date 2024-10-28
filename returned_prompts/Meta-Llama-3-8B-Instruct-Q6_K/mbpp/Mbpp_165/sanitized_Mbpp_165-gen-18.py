def count_char_position(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = s.lower()
    count = 0
    for i in range(len(s)):
        if s[i] in alphabet and i == alphabet.index(s[i]):
            count += 1
    return count