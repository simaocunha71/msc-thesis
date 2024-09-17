def check_smaller(t1, t2):
    for i in range(min(len(t1), len(t2))):
        if t1[i] <= t2[i]:
            return False
    return True