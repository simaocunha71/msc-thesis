def get_equal(tup):
    l = len(tup[0])
    for i in tup:
        if len(i) != l:
            return False
    return True