def sample_nam(names):
    sum_ = 0
    for name in names:
        if not name[0].islower():
            sum_ += len(name)
    return sum_