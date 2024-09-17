def max_sub_array_sum_repeated(test_list, n, k):
    test_list = test_list * k
    max_sum = float('-inf')
    current_sum = 0
    for i in range(len(test_list)):
        current_sum += test_list[i]
        if i >= n:
            current_sum -= test_list[i-n]
        if i >= n-1:
            max_sum = max(max_sum, current_sum)
    return max_sum