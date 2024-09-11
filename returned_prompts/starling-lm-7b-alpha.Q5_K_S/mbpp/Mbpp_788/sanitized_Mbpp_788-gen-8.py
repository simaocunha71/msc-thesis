def new_tuple(list1, string1):
    # Converting the string to list
    lst_from_str = list(string1)
    # Converting the list to tuple
    tuple_from_list = tuple(lst_from_str + list1)
    # Returning the tuple
    return tuple_from_list