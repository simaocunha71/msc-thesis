def find_substring(lst, substring):
    for string in lst:
        if substring in string:
            return True
    return False