def find_substring(list_strs, sub_str):
    for i in range(len(list_strs)):
        if sub_str in list_strs[i]:
            return True
    return False