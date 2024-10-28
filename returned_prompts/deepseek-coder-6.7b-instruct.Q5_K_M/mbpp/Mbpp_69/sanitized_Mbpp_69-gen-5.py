def is_sublist(main_list, sublist):
    for i in range(len(main_list)):
        if main_list[i:i+len(sublist)] == sublist:
            return True
    return False