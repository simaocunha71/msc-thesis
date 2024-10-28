def get_equal(lst):
    for tup in lst:
        if len(tup) != len(lst[0]):
            return False
    return True