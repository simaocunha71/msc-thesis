def add_string(lst: list, pattern: str) -> list:
    return [pattern.format(i) for i in lst]