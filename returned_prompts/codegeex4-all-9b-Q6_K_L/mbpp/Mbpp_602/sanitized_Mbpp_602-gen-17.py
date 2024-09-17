def first_repeated_char(s: str) -> str:
    return next((char for char in s if s.count(char) > 1), None)