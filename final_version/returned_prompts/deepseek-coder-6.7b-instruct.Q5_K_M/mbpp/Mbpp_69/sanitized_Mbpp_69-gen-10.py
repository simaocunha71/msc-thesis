def is_sublist(main_list, sublist):
    return all(item in main_list for item in sublist)