"""
def dict_depth(my_dict):
    return len(my_dict) if not isinstance(my_dict, dict) else 1 + max(dict_depth(v) for v in my_dict.values())
"""
