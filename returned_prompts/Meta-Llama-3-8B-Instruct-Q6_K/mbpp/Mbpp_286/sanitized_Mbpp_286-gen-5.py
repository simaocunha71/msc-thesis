def max_sub_array_sum_repeated(arr, k, max_length):
    max_sum = float('-inf')
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            total_sum = sum(arr[i:j+1])
            if total_sum > max_sum:
                max_sum = total_sum
    return max_sum