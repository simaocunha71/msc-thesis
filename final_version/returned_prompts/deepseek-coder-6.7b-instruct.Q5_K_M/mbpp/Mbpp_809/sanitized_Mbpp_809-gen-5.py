def check_smaller(t1, t2):
    for i, j in zip(t1, t2):
        if i >= j:
            return False
    return True