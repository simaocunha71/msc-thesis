def max_sub_array_sum_repeated(arr, k, n):
    modified_arr = arr * k
    max_sum = float('-inf')
    for i in range(len(modified_arr)):
        temp = 0
        for j in range(i, len(modified_arr)):
            temp += modified_arr[j]
            if temp > max_sum:
                max_sum = temp
    return max_sum