def count_reverse_pairs(lst):
    count = 0
    for s in lst:
        if s[::-1] in lst:
            count += 1
    return count