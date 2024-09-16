"""
def max_sub_array_sum_repeated(arr, k, n):
    if k == 1:
        return max(arr)
    if k == n:
        return sum(arr)
    if n == 1:
        return arr[0]

    max_k_times_sum = 0
    max_sum_in_current_window = 0

    for i in range(n):
        max_sum_in_current_window += arr[i]
        max_k_times_sum = max(max_k_times_sum, max_sum_in_current_window)
        max_sum_in_current_window = max(max_sum_in_current_window, 0)

    return max(max_k_times_sum, max_sub_array_sum_repeated(arr, k - 1, n - 1))
"""