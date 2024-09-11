def check_smaller(tup1, tup2):
    for i in range(len(tup1)):
        if tup2[i] <= tup1[i]:
            return False
    return True