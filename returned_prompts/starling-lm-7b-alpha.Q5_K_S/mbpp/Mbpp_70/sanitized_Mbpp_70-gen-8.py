def get_equal(lst):
    result = True
    for t in lst:
        if len(t) != len(lst[0]):
            result = False
            break
    return result