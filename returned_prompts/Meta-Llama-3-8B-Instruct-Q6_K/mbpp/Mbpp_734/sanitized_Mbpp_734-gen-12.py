def sum_Of_Subarray_Prod(lst):
    total_sum = 0
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            total_sum += sum([lst[k] for k in range(i, j+1)])
    return total_sum