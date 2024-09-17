def find_substring(lst, substr):
    for item in lst:
        if substr in item:
            return True
    return False