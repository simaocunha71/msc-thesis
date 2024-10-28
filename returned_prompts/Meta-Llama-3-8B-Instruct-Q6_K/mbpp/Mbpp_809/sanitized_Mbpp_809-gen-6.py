def check_smaller(t1, t2):
    return all(i >= j for i, j in zip(t1, t2)) == False