
def is_sublist(list1, list2):
    for i in range(len(list1)):
        if list1[i:] == list2:
            return True
    return False


