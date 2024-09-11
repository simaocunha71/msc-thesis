def find_substring(lst, substring):
    return any(substring in s for s in lst)  # returns True if the substring is found in any string in the list, False otherwise.