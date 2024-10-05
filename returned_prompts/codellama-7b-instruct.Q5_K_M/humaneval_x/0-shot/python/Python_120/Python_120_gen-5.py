
def maximum(arr, k):
    """
    :type arr: List[int]
    :type k: int
    :rtype: List[int]
    """
    if k == 0:
        return []
    elif k == 1:
        return [max(arr)]
    else:
        arr.sort()
        arr.reverse()
        return arr[:k]
