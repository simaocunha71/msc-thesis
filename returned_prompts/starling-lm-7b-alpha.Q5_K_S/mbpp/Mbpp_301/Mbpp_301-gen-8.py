def dict_depth(d):
    depth = 0
    for k, v in d.items():
        if isinstance(v, dict):
            depth = max(depth, dict_depth(v) + 1)
    return depth


def dict_depth_v2(d):
    return 1 + max(map(dict_depth_v2, d.values()) + [0] if isinstance(d[k], dict) else [0] for k in d)


# print(dict_depth_v2({'a': 1, 'b': {'c': {'d': {}}}}))


from collections import defaultdict

def dict_depth_v3(d):
    if isinstance(d, defaultdict):
        return 1 + max(map(dict_depth_v3, d.values()) + [0] if isinstance(d[k], dict) else [0] for k in d)
    else:
        return 0

# print(dict_depth_v3(defaultdict(dict, {'a': 1, 'b': {'c': {'d': {}}}})))


def dict_depth_v4(d):
    if isinstance(d, dict):
        return 1 + max(map(dict_depth_v4, d.values()) + [0] if isinstance(d[k], dict) else [0] for k in d)
    else:
        return 0

# print(dict_depth_v4({'a': 1, 'b': {'c': {'d': {}}}}))


def dict_depth_v5(d):
    return 1 + max(map(dict_depth_v5, d.values()) + [0] if isinstance(d[k], dict) else [0] for k in d) if isinstance(d, dict) else 0

# print(dict_depth_v5({'a': 1, 'b': {'c': {'d': {}}}}))


def dict_depth_v6(d):
    if isinstance(d, dict):
        return 1 + max(map(dict_depth_v6, d.values()) + [0] if isinstance