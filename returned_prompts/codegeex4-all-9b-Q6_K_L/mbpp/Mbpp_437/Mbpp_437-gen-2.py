def remove_odd(s: str) -> str:
    return ''.join([char for char in s if s.index(char) % 2 == 0])

