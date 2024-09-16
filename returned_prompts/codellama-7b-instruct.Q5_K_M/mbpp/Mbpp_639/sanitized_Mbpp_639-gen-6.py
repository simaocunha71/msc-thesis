def sample_nam(names):
    lowercase_names = [name for name in names if name[0].islower()]
    return sum(len(name) for name in names if name not in lowercase_names)