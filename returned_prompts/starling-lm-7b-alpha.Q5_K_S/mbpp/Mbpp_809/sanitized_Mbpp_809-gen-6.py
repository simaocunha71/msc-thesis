def check_smaller(t1, t2):
    return all(a < b for a, b in zip(t1, t2))