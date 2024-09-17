def sample_nam(names: list) -> int:
    return sum(len(name) for name in names if name[0].isupper())

