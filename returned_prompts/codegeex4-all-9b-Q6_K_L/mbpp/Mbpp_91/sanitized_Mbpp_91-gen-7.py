def find_substring(lst, substring):
    for word in lst:
        if substring in word:
            return True
    return False