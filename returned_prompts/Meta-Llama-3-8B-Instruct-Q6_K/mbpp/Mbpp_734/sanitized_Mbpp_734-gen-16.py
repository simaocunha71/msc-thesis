def sum_Of_Subarray_Prod(lst):
    total_sum = 0
    prefix_sum = [0] * (len(lst) + 1)
    for i in range(len(lst)):
        prefix_sum[i+1] = prefix_sum[i] + lst[i]
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            total_sum += (prefix_sum[j+1] - prefix_sum[i]) * (prefix_sum[j+1] - prefix_sum[i])
    return total_sum