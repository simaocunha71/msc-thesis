def count_char_position(s: str) -> int:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    count = 0
    for i in range(len(s)):
        if s[i].lower() == alphabet[i]:
            count += 1
    return count

