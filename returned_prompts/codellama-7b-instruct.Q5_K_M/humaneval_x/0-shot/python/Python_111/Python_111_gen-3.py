
def histogram(test):
    test = test.split(' ')
    test_dict = {}
    for i in test:
        if i in test_dict:
            test_dict[i] += 1
        else:
            test_dict[i] = 1
    return test_dict
