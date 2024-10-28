def is_sublist(main_list, sublist):
    if sublist == []:
        return True
    if sublist[0] not in main_list:
        return False
    index = main_list.index(sublist[0])
    if main_list[index:index+len(sublist)] == sublist:
        return True
    return False