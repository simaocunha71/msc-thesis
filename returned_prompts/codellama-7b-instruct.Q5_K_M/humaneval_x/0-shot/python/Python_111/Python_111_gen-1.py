
def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    test = test.split()
    histogram = dict()
    for i in test:
        if i in histogram.keys():
            histogram[i] += 1
        else:
            histogram[i] = 1
    maxi = 0
    maxi_key = None
    for key, value in histogram.items():
        if value > maxi:
            maxi = value
            maxi_key = key
    if maxi_key == None:
        return {}
    else:
        return {maxi_key: maxi}
