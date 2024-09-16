
def min_k(lst, k):
    return sorted(lst, key=lambda x: x[1])[:k]
