def find_tuples(tuples_list, k):
    result = []
    for t in tuples_list:
        if all(i % k == 0 for i in t):
            result.append(t)
    return result