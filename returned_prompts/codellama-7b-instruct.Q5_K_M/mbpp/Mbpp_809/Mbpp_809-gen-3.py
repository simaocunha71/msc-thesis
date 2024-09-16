def check_smaller(t1, t2):
    return all(t1[i] < t2[i] for i in range(len(t1)))
