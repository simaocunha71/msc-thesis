def find_substring(string_list,sub_str):
    for i in string_list:
        if sub_str in i:
            return True
    return False