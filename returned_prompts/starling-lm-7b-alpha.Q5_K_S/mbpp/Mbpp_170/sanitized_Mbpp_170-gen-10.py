def sum_range_list(lst, i, j):
    total = 0
    for index in range(i, j + 1):
        total += lst[index]
    return total