def sum_Of_Subarray_Prod(lst):
    total = 0
    for i in range(len(lst) + 1):
        for j in range(i + 1, len(lst) + 1):
            total += math.prod(lst[i:j])
    return total