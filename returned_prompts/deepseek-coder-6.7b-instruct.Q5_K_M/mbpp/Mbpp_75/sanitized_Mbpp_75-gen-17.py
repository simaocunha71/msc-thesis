def find_tuples(tuples_list, k):
    return [t for t in tuples_list if all(x % k == 0 for x in t)]