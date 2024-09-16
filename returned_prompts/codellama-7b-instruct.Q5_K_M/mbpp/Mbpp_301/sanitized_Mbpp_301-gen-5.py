def dict_depth(dct):
    """
    Returns the depth of a dictionary.
    """
    depth = 1
    for v in dct.values():
        if isinstance(v, dict):
            depth = max(depth, dict_depth(v)+1)
    return depth