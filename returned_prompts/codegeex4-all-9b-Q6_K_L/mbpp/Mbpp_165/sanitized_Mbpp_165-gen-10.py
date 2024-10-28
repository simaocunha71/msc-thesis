def count_char_position(s: str) -> int:
    count = 0
    s = s.lower()
    for i in range(len(s)):
        if s[i] == chr(ord('a') + i):
            count += 1
    return count