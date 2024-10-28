
def max_sum_increasing_subseq(arr: list, n: int, k: int, i: int) -> int:
    if i == k or i == -1:
        return 0
    if arr[i] > arr[k]:
        return max(arr[i], max_sum_increasing_subseq(arr, n, k-1, i))
    else:
        return max(arr[i], max_sum_increasing_subseq(arr, n, k-1, i-1))


