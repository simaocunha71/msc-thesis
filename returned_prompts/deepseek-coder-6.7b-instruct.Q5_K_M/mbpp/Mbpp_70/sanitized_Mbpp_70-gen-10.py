def get_equal(tuples):
    length = len(tuples[0])
    for tup in tuples:
        if len(tup) != length:
            return False
    return True