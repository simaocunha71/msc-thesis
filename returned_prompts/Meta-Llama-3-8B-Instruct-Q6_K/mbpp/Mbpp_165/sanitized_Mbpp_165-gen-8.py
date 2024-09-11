def count_char_position(s: str) -> int:
    s = s.lower()
    count = 0
    for i in range(len(s)):
        if ord('a') <= ord(s[i]) <= ord('z') and ord(s[i]) - ord('a') == i:
            count += 1
    return count