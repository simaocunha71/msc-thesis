def find_substring(list_of_strings, substring):
    for i in list_of_strings:
        if substring in i:
            return True
    return False