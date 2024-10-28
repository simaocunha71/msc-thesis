def find_substring(lst, substring):
    for s in lst:
        if substring in s:
            return True
    return False