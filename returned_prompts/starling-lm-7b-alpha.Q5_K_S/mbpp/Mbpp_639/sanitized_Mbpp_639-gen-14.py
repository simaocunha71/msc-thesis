def sample_nam(names):
    names = [name for name in names if name[0].isupper()]
    return sum(len(name) for name in names)