def max_sum_increasing_subseq(arr: list, length: int, i: int, k: int) -> int:
    if i >= length or k >= length or k <= i:
        return 0
    else:
        return arr[i] + arr[k] + max(max_sum_increasing_subseq(arr, length, i+1, k+1),
 max_sum_increasing_subseq(arr, length, i+1, k))