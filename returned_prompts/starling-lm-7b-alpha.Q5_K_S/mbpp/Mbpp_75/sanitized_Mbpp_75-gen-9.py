def find_tuples(tuples, k):
    result = []
    for tup in tuples:
        if all(i % k == 0 for i in tup):
            result.append(tup)
    return result