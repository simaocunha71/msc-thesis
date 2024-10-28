
def Find_Min_Length(list_of_lists):
    if not list_of_lists:
        return 0
    return min(len(lst) for lst in list_of_lists)


