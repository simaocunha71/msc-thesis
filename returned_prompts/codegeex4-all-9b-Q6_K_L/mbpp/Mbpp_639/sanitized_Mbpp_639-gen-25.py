def sample_nam(names: list) -> int:
    name_lengths = [len(name) for name in names if name[0].isupper()]
    return sum(name_lengths)