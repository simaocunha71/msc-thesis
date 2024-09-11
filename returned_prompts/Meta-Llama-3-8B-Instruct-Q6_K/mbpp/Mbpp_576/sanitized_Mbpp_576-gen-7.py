def is_Sub_Array(list1, list2):
    for i in range(len(list1)):
        if list1[i:i+len(list2)] == list2:
            return True
    return False