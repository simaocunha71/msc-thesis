def sample_nam(names: list) -> int:
    sum = 0
    for name in names:
        if not name[0].islower():
            sum += len(name)
    return sum