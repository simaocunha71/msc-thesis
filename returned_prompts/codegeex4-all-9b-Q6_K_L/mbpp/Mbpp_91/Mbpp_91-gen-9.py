def find_substring(lst: list, substring: str) -> bool:
    for string in lst:
        if substring in string:
            return True
    return False

