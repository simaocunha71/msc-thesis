def extract_string(string_list, size):
    result_list = []
    for string in string_list:
        if len(string) <= size:
            result_list.append(string)
    return result_list