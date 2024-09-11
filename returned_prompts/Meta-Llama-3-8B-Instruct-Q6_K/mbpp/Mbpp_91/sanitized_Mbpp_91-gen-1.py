def find_substring(lst, substr):
    for s in lst:
        if substr in s:
            return True
    return False