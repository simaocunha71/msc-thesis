def extract_string(lst: list, n: int) -> list:
    return [item for item in lst if len(item) == n]