def check_K(tuples, k):
    for tuple in tuples:
        if k in tuple:
            return True
    return False