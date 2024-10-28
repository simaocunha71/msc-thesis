
def sample_nam(names: list) -> int:
    total_length = 0
    for name in names:
        if name[0].isupper():
            total_length += len(name)
    return total_length


