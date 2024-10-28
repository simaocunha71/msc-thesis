def check_smaller(t1, t2):
    for i in range(len(t1)):
        if t2[i] >= t1[i]:
            return False
    return True