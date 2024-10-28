def get_equal(tuples):
    if len(tuples) == 0:
        return True
    first_length = len(tuples[0])
    for t in tuples:
        if len(t) != first_length:
            return False
    return True