def count_reverse_pairs(lst):
    count = 0
    for i in lst:
        for j in lst:
            if i != j and i == j[::-1]:
                count += 1
    return count