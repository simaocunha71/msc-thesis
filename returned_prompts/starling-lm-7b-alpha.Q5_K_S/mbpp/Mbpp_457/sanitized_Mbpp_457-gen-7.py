def Find_Min(sublist):
    """
    Finds the sublist with minimum length
    """
    sublist_length = len(sublist[0])
    for i in range(1,len(sublist)):
        if len(sublist[i]) < sublist_length:
            sublist_length = len(sublist[i])
    return sublist_length