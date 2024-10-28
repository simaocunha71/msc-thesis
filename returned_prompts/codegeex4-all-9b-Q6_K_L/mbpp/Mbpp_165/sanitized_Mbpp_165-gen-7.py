def count_char_position(s):
    count = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(s)):
        if s[i].lower() == alphabet[i]:
            count += 1
    return count