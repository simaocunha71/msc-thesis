def new_tuple(strings: list, list_elements: str) -> tuple:
    return tuple(list_elements + " " + string for string in strings)