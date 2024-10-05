
def search(lst):
    """
    :type lst: List[int]
    :rtype: int
    """
    m = {}
    for i in lst:
        if i not in m:
            m[i] = 1
        else:
            m[i] += 1
    for k in m:
        if m[k] >= k:
            return k
    return -1
