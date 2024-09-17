
def max_sub_array_sum_repeated(arr, k, n):
    if k == 0:
        return sum(arr)
    if n == 0:
        return 0
    curr_sum = max(0, max_sub_array_sum_repeated(arr, k - 1, n))
    return max(curr_sum, max_sub_array_sum_repeated(arr, k - 1, n - 1) + arr[-n])


