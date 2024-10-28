def find_tuples(lst, k):
    result = [t for t in lst if all(i % k == 0 for i in t)]
    return result