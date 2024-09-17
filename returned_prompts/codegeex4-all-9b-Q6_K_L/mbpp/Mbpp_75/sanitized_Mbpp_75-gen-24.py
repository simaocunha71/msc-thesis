def find_tuples(tuples_list, k):
    result = []
    for tup in tuples_list:
        if all(i % k == 0 for i in tup):
            result.append(tup)
    return result