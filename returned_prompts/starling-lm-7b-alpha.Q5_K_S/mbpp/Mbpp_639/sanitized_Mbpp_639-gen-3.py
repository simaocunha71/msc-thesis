def sample_nam(names):
    length = 0
    for name in names:
        if name[0].isupper():
            length += len(name)
    return length