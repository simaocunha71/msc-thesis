def check_smaller(t1, t2):
    if len(t1) != len(t2):
        return False
    for i in range(len(t1)):
        if t2[i] >= t1[i]:
            return False
    return True