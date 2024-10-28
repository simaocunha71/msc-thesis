
def find_tuples(tuples, k):
    return [t for t in tuples if all(i % k == 0 for i in t)]
