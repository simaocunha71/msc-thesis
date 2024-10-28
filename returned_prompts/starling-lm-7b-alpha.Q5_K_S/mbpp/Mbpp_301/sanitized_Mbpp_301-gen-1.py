from collections import defaultdict
from collections import defaultdict
from collections import defaultdict
def dict_depth(d):
    if isinstance(d, dict):
        return 1 + max(map(dict_depth, d.values()))
    elif isinstance(d, list):
        return 1 + max(map(dict_depth, d))
    else:
        return 0