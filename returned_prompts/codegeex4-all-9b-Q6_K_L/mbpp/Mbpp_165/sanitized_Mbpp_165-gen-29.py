def count_char_position(s: str) -> int:
    count = 0
    s = s.lower()
    for i in range(len(s)):
        if ord(s[i]) - 97 == i:
            count += 1
    return count