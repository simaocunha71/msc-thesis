def replace_list(list1, list2):
    '''This function takes in two lists and replaces the last element of the first list with the elements of the second list.'''
    list1.pop()
    list1.extend(list2)
    return list1