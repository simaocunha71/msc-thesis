def is_sublist(mainlist,sublist):
    for i in range(len(mainlist)-len(sublist)+1):
        if mainlist[i:i+len(sublist)]==sublist:
            return True
    return False