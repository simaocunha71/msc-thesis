def overlapping(list1:list,list2:list) -> bool:
    if any(i in list2 for i in list1):
        return True
    else:
        return False