
def count_char_position(s: str) -> int:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    for i,c in enumerate(s.lower()):
        if c == alphabet[i]:
            count += 1
    return count


