def find_substring(list_strings, string):
    for i in list_strings:
        if string in i:
            return True
    return False