def max_sum_increasing_subseq(arr: list, n: int, i: int, k: int) -> int:
    if k < i:
        return 0
    if i == k:
        return arr[i]

    max_sum = 0
    for j in range(i, k):
        curr_sum = arr[j] + max(max_sum_increasing_subseq(arr, n, i, j),
                                max_sum_increasing_subseq(arr, n, j + 1, k))
        max_sum = max(max_sum, curr_sum)
    return max_sum