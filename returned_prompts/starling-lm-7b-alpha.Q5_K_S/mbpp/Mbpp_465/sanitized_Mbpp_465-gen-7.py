from collections import defaultdict
def drop_empty(d):
    return defaultdict(list, {k: v for k, v in d.items() if v})