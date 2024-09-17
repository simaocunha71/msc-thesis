def find_substring(lst, target):
    for word in lst:
        if target in word:
            return True
    return False