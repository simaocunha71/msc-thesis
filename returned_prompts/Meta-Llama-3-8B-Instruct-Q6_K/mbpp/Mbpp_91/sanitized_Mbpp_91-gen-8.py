def find_substring(lst, sub):
    for s in lst:
        if sub in s:
            return True
    return False