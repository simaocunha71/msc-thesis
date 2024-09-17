
def find_tuples(tuples, k):
    return list(filter(lambda x: all(i % k == 0 for i in x), tuples))


