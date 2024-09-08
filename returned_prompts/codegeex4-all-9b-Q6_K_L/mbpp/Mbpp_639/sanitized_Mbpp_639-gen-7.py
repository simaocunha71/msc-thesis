def sample_nam(lst):
    total_length = 0
    for name in lst:
        if name[0].isupper():
            total_length += len(name)
    return total_length