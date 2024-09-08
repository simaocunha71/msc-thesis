def check_smaller(t1, t2):
    for i in range(len(t1)):
        if not t1[i] < t2[i]:
            return False
    return True