def number_ctr(string: str) -> int:
    return sum(c.isdigit() for c in string)