def find_substring(my_list: list, substring: str) -> bool:
    for item in my_list:
        if substring in item:
            return True
    return False