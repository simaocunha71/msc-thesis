def find_substring(lst, substr):
    for word in lst:
        if substr in word:
            return True
    return False