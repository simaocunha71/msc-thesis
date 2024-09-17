def check_K(tuples, k):
    k = str(k)
    for tuple in tuples:
        if k in str(tuple):
            return True
    return False