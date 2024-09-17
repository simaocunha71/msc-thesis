
def check_type(test_tup):
    return all(isinstance(i, type(test_tup[0])) for i in test_tup)


