"""
def dict_depth(d):
    return max(d.values(), default=0, key=dict_depth) + 1
"""
