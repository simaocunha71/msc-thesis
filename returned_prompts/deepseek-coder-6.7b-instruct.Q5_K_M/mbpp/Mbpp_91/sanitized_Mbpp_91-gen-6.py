def find_substring(list_str, substr):
    for string in list_str:
        if substr in string:
            return True
    return False