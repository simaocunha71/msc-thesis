def count_reverse_pairs(lst):
    count = 0
    for s in lst:
        if s == s[::-1]:
            count += 1
    return count