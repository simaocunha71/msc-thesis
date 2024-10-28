def max_sub_array_sum_repeated(arr, k, n):
    # calculating the total sum of the array
    total_sum = sum(arr)

    # calculating the sum of the array after it is repeated k times
    arr_sum = sum(arr * k)

    # calculating the maximum sub-array sum
    max_sum = max(arr_sum, total_sum * (k - 1))

    # returning the maximum sum
    return max_sum