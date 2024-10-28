def sample_nam(names):
    count = 0
    for name in names:
        if name[0].isupper():
            count += len(name)
    return count