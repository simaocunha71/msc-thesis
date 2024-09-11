def max_sub_array_sum_repeated(arr, k, m):
    max_sum = float('-inf')
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            temp_sum = sum(arr[i:j+1])
            if temp_sum > max_sum:
                max_sum = temp_sum
    return max_sum * k % m