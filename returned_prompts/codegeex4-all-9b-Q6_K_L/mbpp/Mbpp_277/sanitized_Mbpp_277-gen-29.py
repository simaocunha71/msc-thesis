def dict_filter(dict1: dict, n: int) -> dict:
    return {k: v for k, v in dict1.items() if v >= n}