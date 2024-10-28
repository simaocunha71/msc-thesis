def get_equal(tuples):
    for t in tuples:
        if len(t) != len(tuples[0]):
            return False
    return True

