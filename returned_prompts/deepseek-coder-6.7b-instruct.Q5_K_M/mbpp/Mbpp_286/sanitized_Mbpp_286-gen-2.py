def max_sub_array_sum_repeated(arr, k, n):
    def kadane(arr):
        max_current = max_global = arr[0]
        for i in range(1, len(arr)):
            max_current = max(arr[i], max_current + arr[i])
            if max_current > max_global:
                max_global = max_current
        return max_global

    arr = arr * k
    return kadane(arr)