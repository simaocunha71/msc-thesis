def sample_nam(names):
    total = 0
    for name in names:
        if name[0].lower() != 'd':
            total += len(name)
    return total