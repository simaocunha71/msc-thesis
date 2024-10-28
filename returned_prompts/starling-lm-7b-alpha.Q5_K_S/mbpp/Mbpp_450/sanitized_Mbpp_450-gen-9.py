def extract_string(list_string, length):
    new_list = []
    for i in list_string:
        if len(i)>=length:
            new_list.append(i)
    return new_list