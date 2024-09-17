def get_equal(tuples):
    for i in range(len(tuples)-1):
        if len(tuples[i]) != len(tuples[i+1]):
            return False
    return True