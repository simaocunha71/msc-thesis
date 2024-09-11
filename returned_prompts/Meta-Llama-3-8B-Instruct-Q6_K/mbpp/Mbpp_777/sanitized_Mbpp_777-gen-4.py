def find_sum(lst):
    return sum(x for x in set(lst) if lst.count(x) == 1)