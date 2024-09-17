def extract_string(string_list, size):
    if size > len(string_list):
        return string_list
    else:
        return string_list[:size]