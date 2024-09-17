def sub_list(list1,list2):
    # your code goes here
    l1 = len(list1)
    l2 = len(list2)
    if l1!=l2:
        return False
    for i in range(l1):
        if list1[i]-list2[i]!=0:
            return False
    return list1-list2