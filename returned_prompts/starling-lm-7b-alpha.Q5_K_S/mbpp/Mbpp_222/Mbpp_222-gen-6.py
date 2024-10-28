
def check_type(test_tup):
    for i in range(len(test_tup)):
        if type(test_tup[i]) != type(test_tup[0]):
            return False
    return True


