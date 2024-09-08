def max_sub_array_sum_repeated(arr, k, n):
    # Modifying the array
    arr = arr * k
    # Getting the sum of the original array
    original_sum = sum(arr)
    # Getting the length of the array
    l = len(arr)
    # Initializing the result as minimum value
    res = float('-inf')
    # For every possible subarray
    for i in range(l):
        for j in range(i, l):
            # Calculating the sum of the subarray
            sub_arr_sum = sum(arr[i:j+1])
            # Updating the result if the sum is greater than the current result
            res = max(res, sub_arr_sum)
    # Returning the result
    return res