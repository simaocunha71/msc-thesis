
def count_char_position(s: str) -> int:
    return sum(1 for i in range(min(len(s), 26)) if chr(97+i) == s[i].lower())


