def get_equal(tuples):
    if len(tuples) == 0:
        return True
    else:
        length = len(tuples[0])
        for tuple in tuples:
            if len(tuple) != length:
                return False
        return True