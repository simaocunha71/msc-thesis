def get_equal(tuples):
    if len(set(map(len, tuples))) == 1:
        return True
    else:
        return False