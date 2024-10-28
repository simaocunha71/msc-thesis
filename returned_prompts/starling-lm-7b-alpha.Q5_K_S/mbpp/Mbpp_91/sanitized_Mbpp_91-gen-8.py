def find_substring(string_list, sub_string):
    for string in string_list:
        if sub_string in string:
            return True
    return False