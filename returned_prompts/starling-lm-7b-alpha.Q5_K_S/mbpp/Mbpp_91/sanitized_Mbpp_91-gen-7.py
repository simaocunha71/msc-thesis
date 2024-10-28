def find_substring(list_of_string, sub_string):
    for item in list_of_string:
        if sub_string in item:
            return True
    return False