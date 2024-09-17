def get_equal(tuples):
    if len(set(len(t) for t in tuples)) == 1:
        return True
    else:
        return False