def max_sub_array_sum(arr, k):
    """
    :type arr: List[int]
    :type k: int
    :rtype: int
    """
    max_sum = -1
    curr_sum = 0

    for i in range(len(arr)):
        curr_sum += arr[i]
        if i > k - 1:
            curr_sum -= arr[i-k]
        if curr_sum > max_sum:
            max_sum = curr_sum

    return max_sum