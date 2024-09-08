def find_substring(lst, sub):
    return any(sub in s for s in lst)