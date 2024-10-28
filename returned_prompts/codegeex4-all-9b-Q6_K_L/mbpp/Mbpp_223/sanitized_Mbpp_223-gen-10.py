def is_majority(arr, n, el):
    """
    Returns True if the element el is the majority element in the sorted array arr.
    """
    count = 0
    for i in range(n):
        if arr[i] == el:
            count += 1
    return count > n // 2