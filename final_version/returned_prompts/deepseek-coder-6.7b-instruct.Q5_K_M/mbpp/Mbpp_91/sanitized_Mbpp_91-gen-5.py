def find_substring(lst, string):
    return any(string in i for i in lst)