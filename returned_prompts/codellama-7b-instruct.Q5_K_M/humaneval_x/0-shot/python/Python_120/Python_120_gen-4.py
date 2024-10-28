
def maximum(arr, k):
    """
    :type arr: List[int]
    :type k: int
    :rtype: List[int]
    """
    return sorted(arr, reverse=True)[:k]
