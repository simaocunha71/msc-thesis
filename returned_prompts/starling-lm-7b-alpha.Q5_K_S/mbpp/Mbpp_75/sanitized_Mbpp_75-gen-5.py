def find_tuples(lst, k):
    result = []
    for tuple in lst:
        if all(i % k == 0 for i in tuple):
            result.append(tuple)
    return result