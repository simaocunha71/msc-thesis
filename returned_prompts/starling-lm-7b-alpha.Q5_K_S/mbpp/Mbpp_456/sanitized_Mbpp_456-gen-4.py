def reverse_string_list(list_strings):
    list_strings = [list_strings[i][::-1] for i in range(len(list_strings))]
    return list_strings