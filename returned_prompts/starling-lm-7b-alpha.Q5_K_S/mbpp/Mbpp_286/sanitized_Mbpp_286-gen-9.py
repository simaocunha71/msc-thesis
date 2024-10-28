def max_sub_array_sum_repeated(array, k, n):
    max_sum = float('-inf')
    for i in range(k):
        cur_sum = 0
        for j in range(i, n):
            cur_sum += array[(j + i) % n]
            max_sum = max(max_sum, cur_sum)
    return max_sum