def get_equal(lst):
    for i in lst:
        if len(i) != len(lst[0]):
            return False
    return True