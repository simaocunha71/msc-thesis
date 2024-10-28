"""
def max_sub_array_sum_repeated(arr, k, n):
    if k == 0:
        return 0
    if k == 1:
        return sum(arr)
    if n == 1:
        return sum(arr)
    return max(
        max_sub_array_sum_repeated(arr[:-1], k - 1, n - 1) + arr[-1],
        max_sub_array_sum_repeated(arr, k, n - 1)
    )
"""
