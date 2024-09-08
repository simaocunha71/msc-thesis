def find_tuples(tuples, k):
    result = []
    for t in tuples:
        if all(i % k == 0 for i in t):
            result.append(t)
    return result