def get_equal(tuples):
    if len(set(len(tup) for tup in tuples)) == 1:
        return True
    else:
        return False