
def is_sublist(list1, sublist):
    if sublist == []:
        return True
    for i in range(len(list1)):
        if list1[i:i+len(sublist)] == sublist:
            return True
    return False


