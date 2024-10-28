def find_tuples(lst, k):
    result = []
    for tup in lst:
        if all(i % k == 0 for i in tup):
            result.append(tup)
    return result