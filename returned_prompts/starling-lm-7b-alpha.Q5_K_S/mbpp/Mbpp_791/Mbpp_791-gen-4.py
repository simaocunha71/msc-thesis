
def remove_nested(test_tup):
    for i in test_tup:
        if isinstance(i, tuple):
            test_tup = test_tup.replace(i, "")
    return test_tup


