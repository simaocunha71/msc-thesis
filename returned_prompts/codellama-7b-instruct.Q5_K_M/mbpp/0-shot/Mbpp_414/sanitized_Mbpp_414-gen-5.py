def overlapping(list1,list2):
    if list1 == list2:
        return True
    else:
        for i in list2:
            if i in list1:
                return True
            else:
                return False