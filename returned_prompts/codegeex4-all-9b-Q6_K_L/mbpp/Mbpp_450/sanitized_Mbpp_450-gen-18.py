def extract_string(string_list: list, size: int) -> list:
    return [x for x in string_list if len(x) == size]