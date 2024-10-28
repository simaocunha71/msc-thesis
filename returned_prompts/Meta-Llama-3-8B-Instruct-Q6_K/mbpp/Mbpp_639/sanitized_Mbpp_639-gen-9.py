def sample_nam(names):
    sum_lengths = 0
    for name in names:
        if name[0].isupper():
            sum_lengths += len(name)
    return sum_lengths