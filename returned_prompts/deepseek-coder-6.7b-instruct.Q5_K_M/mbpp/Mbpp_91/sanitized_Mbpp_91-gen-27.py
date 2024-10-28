def find_substring(lst, sub):
    return any(sub in i for i in lst)