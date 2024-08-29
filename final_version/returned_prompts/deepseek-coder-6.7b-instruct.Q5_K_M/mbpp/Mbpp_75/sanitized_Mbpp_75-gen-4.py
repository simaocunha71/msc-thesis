def find_tuples(lst, k):
    return [tup for tup in lst if all(el % k == 0 for el in tup)]