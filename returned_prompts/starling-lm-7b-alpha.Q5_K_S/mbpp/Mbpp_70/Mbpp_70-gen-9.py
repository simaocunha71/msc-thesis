
def get_equal(test_tup):
    for i in range(len(test_tup)):
        if len(test_tup[i])!=len(test_tup[0]):
            return False
    return True


