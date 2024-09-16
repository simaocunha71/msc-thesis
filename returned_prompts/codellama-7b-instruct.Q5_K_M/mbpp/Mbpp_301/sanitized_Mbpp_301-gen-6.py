import collections
def dict_depth(d):
    if not isinstance(d, collections.Mapping):
        return 0
    return 1 + max(dict_depth(v) for v in d.values())