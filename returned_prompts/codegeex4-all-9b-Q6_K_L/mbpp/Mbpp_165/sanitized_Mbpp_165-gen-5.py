def count_char_position(s: str) -> int:
    count = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i, c in enumerate(s.lower()):
        if i < len(alphabet) and c == alphabet[i]:
            count += 1
    return count