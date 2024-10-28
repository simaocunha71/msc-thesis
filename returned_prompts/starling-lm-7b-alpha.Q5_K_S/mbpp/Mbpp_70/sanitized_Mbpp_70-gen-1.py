def get_equal(list_of_tuples):
    if len(list_of_tuples) == 0:
        return True
    length = len(list_of_tuples[0])
    for i in list_of_tuples:
        if len(i) != length:
            return False
    return True