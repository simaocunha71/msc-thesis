def max_sub_array_sum_repeated(arr: list, k: int, t: int) -> int:
    # get the maximum sub array sum
    def kadane(arr):
        max_current = max_global = arr[0]
        for i in range(1, len(arr)):
            max_current = max(arr[i], max_current + arr[i])
            if max_current > max_global:
                max_global = max_current
        return max_global

    n = len(arr)
    arr_repeated = arr * k
    max_sum = 0

    for i in range(n):
        for j in range(i + n, len(arr_repeated)):
            if j - i + 1 > n * t:
                continue
            max_sum = max(max_sum, kadane(arr_repeated[i:j + 1]))

    return max_sum