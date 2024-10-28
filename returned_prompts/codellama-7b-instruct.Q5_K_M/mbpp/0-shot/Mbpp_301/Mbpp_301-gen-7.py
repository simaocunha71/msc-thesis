"""
def dict_depth(d):
    depth = 1
    for v in d.values():
        if isinstance(v, dict):
            depth = max(depth, dict_depth(v)+1)
    return depth
"""
