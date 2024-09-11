def Diff(list1, list2):
    return (list(set(list1) - set(list2)) + list(set(list2) - set(list1))) 
    # set(list1) - set(list2) returns the elements in list1 that are not in list2
    # set(list2) - set(list1) returns the elements in list2 that are not in list1
    # We add the two results together, which removes duplicates and returns the difference between the two lists
    # We convert the result back to a list and return it