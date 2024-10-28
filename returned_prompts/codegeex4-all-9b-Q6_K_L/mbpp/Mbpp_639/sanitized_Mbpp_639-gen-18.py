def sample_nam(names):
    new_names = [name for name in names if name[0].isupper()]
    return sum(len(name) for name in new_names)