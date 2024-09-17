def sample_nam(names: list) -> int:
    total = 0
    for name in names:
        if not name[0].islower():
            total += len(name)
    return total