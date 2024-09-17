
def min_k(tuples, k):
    tuples.sort(key=lambda x: x[1])
    return tuples[:k]


