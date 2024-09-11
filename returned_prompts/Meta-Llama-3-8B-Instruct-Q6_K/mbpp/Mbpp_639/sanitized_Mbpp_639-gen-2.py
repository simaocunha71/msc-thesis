def sample_nam(names):
    return sum(len(name) for name in names if name[0].isupper())  # sum of lengths of names that start with uppercase letter