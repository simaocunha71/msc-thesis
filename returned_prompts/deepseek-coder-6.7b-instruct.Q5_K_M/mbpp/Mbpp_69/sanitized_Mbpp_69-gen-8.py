def is_sublist(main_list, sub_list):
    return all(item in main_list for item in sub_list)