def max_subarray_product(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    max_product = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_product:
            max_product = arr[i]
        if arr[i] < 0:
            max_product = arr[i-1]
    return max_product