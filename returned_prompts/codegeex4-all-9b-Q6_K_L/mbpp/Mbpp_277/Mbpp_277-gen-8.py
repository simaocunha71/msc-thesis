def dict_filter(dictionary: dict,n: int) -> dict:
    return {key: value for key, value in dictionary.items() if value >= n}