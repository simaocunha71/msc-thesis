def count_reverse_pairs(lst):
    return sum(1 for s in lst if s == s[::-1]) // 2