def is_Sub_Array(list1,list2):
    for i in range(len(list2)-len(list1)+1):
        if list1 == list2[i:i+len(list1)]:
            return True
    return False