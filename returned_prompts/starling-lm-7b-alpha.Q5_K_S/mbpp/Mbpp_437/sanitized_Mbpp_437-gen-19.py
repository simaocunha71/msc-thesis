def remove_odd(s: str) -> str:
    return ''.join(filter(lambda x: int(x) % 2 == 0, s))