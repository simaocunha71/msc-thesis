from collections import defaultdict
def dict_depth(d):
    depth = 0
    for k, v in d.items():
        if isinstance(v, dict):
            depth = max(depth, dict_depth(v) + 1)
    return depth