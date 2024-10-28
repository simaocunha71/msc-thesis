def max_sub_array_sum_repeated(arr: list, k: int, n: int) -> int:
    if k == 1:
        return sum(arr)
    return sum(arr) + max(max_sub_array_sum_repeated(arr, k - 1, n - 1), 0)