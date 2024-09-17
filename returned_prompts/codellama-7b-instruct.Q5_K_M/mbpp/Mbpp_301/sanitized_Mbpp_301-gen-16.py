def dict_depth(my_dict: dict):
    if not my_dict:
        return 0
    return 1 + max(dict_depth(v) for v in my_dict.values())