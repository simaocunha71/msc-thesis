def dict_depth(d):
    res = 0
    for k, v in d.items():
        if isinstance(v, dict):
            res = max(res, dict_depth(v)+1)
    return res

def dict_depth(d):
    if isinstance(d, dict):
        return 1 + max(map(dict_depth, d.values()))
    else:
        return 0

def dict_depth(d):
    return 0 if not d else max(map(dict_depth, d.values())) + 1

def dict_depth(d):
    if isinstance(d, dict):
        return 1 + max([dict_depth(i) for i in d.values()])
    else:
        return 0

def dict_depth(d):
    if isinstance(d, dict):
        return 1 + max([dict_depth(v) for v in d.values()])
    else:
        return 0

def dict_depth(d):
    if isinstance(d, dict):
        return max(dict_depth(v) for v in d.values()) + 1
    else:
        return 0

def dict_depth(d):
    if isinstance(d, dict):
        return 1 + max(dict_depth(v) for v in d.values())
    else:
        return 0

def dict_depth(d):
    if isinstance(d, dict):
        return 1 + max(dict_depth(v) for v in d.values())
    else:
        return 0

def dict_depth(d):
    if isinstance(d, dict):
        return max(dict_depth(v) for v in d.values()) + 1
    else:
        return 0

def dict_depth(d):
    if isinstance(d, dict):
        return 1 + max(dict_depth(v) for v in d.values())
    else:
        return 0

def dict_depth(d):
    if isinstance(d, dict):
        return max(dict_depth(v) for v in d.values()) + 1
    else: