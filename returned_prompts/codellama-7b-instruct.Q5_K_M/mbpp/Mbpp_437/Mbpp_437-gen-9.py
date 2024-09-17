
def remove_odd(s: str) -> str:
    return ''.join([c for i, c in enumerate(s) if i % 2])


