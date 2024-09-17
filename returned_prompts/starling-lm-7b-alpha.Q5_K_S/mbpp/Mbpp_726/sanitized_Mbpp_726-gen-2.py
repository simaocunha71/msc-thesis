def multiply_elements(t):
    """
    :type t: Tuple[int, ...]
    :rtype: Tuple[int, ...]
    """
    return tuple(t[i]*t[i+1] for i in range(len(t)-1))