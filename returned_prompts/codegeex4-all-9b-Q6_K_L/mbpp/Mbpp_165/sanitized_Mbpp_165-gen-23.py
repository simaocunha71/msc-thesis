def count_char_position(s: str) -> int:
    count = 0
    for i in range(len(s)):
        if s[i].lower() == chr(ord('a') + i):
            count += 1
    return count