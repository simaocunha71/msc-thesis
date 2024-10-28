def count_char_position(s: str) -> int:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    for i, char in enumerate(s.lower()):
        if char in alphabet and i == alphabet.index(char):
            count += 1
    return count