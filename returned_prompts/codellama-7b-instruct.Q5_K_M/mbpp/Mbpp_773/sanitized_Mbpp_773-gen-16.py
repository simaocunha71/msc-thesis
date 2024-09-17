def occurance_substring(main_string, search_string):
    if search_string in main_string:
        return (search_string, main_string.index(search_string), main_string.index(search_string) + len(search_string))
    else:
        return None