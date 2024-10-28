def is_sublist(list,sublist):
    for i in range(len(list)-len(sublist)+1):
        if list[i:i+len(sublist)] == sublist:
            return True
    return False