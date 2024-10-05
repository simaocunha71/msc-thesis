
def histogram(test):
    test_list = test.split(' ')
    hist = {}
    for i in test_list:
        if i not in hist:
            hist[i] = 1
        else:
            hist[i] += 1
    return hist
