def count_reverse_pairs(lst):
    count = 0
    for word in lst:
        if word[::-1] in lst:
            count += 1
    return count