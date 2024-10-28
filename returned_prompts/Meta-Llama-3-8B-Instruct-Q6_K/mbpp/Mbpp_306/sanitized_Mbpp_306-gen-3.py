def max_sum_increasing_subseq(arr, i, k, j):
    max_sum = 0
    current_sum = 0
    for num in arr[:i]:
        if num < arr[i]:
            current_sum += num
        else:
            max_sum = max(max_sum, current_sum)
            current_sum = 0
    max_sum = max(max_sum, current_sum)
    current_sum = 0
    for num in arr[i:j]:
        if num > arr[i]:
            current_sum += num
        else:
            max_sum = max(max_sum, current_sum + num)
            current_sum = 0
    max_sum = max(max_sum, current_sum + arr[k])
    return max_sum