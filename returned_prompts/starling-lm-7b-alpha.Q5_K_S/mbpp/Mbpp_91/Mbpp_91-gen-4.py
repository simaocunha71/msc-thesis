
def find_substring(list_strings, sub_string):
    for s in list_strings:
        if sub_string in s:
            return True
    return False


