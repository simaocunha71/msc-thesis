def check_smaller(tup1,tup2):
    for i in range(len(tup1)):
        if tup1[i]>tup2[i]:
            return False
    return True