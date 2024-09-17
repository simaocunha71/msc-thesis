def count_char_position(s):
    count = 0
    for i in range(len(s)):
        if ord(s[i].lower()) - 97 == i:
            count += 1
    return count