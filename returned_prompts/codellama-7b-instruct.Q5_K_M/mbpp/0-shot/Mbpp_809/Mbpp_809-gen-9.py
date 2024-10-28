def check_smaller(t1, t2):
    return all(t2_i < t1_i for t1_i, t2_i in zip(t1, t2))

