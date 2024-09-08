def swap_List(lst):
    # store the first element in a variable
    first_element = lst[0]
    
    # store the last element in a variable
    last_element = lst[-1]
    
    # replace the first element with the last element
    lst[0] = last_element
    
    # replace the last element with the first element
    lst[-1] = first_element
    
    return lst