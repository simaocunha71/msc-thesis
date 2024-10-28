def sub_list(l1, l2):
    """
    :type l1: List[int]
    :type l2: List[int]
    :rtype: List[int]
    """
    return [a - b for a, b in zip(l1, l2)]