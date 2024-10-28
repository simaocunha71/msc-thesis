def sample_nam(names: list) -> int:
    names = [name for name in names if not name[0].islower()]
    return sum(len(name) for name in names)