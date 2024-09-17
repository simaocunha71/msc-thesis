def get_equal(tup):
    return all(len(t) == len(tup[0]) for t in tup)