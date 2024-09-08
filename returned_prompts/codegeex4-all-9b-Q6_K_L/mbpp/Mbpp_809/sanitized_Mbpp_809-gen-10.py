def check_smaller(t1, t2):
    if len(t1) != len(t2):
        return False
    return all(t1[i] < t2[i] for i in range(len(t1)))