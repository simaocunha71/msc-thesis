
def is_sublist(list1,sublist):
    for i in range(len(list1)-len(sublist)+1):
        if list1[i:i+len(sublist)] == sublist:
            return True
    return False


