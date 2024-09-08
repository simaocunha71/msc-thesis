def find_tuples(lst, k):
    result = []
    for t in lst:
        if all(i % k == 0 for i in t):
            result.append(t)
    return result