def find_substring(lst, target):
    for string in lst:
        if target in string:
            return True
    return False