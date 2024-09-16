def occurance_substring(main_string, search_string):
    start = main_string.find(search_string)
    if start == -1:
        return None
    else:
        end = start + len(search_string)
        return search_string, start, end



