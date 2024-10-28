def find_sum(lst):
    return sum(set(lst)) - sum(lst.count(i) > 1 for i in lst) * 2