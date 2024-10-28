def dict_depth(dictionary:dict) -> int:
    max_depth = 0
    for k, v in dictionary.items():
        if isinstance(v, dict):
            max_depth = max(max_depth, dict_depth(v) + 1)
    return max_depth