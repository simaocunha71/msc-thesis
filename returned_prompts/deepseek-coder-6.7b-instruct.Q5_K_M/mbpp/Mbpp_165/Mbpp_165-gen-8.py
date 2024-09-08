def count_char_position(s):
    count = 0
    for i in range(len(s)):
        if chr(97 + i).lower() == s[i].lower():
            count += 1
    return count

print(count_char_position("xbcefg"))  # 2


"""
2.
