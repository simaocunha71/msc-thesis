def sort_numeric_strings(strings: list) -> list:
    return sorted(strings, key=lambda x: int(x))