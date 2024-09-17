def reverse_string_list(list):
    list_rev = []
    for item in list:
        list_rev.append(item[::-1])
    return list_rev