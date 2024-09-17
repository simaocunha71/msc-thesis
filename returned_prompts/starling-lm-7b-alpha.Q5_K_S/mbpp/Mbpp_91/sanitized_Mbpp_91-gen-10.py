def find_substring(lst, s):
    for i in range(len(lst)):
        if s in lst[i]:
            return True
    return False