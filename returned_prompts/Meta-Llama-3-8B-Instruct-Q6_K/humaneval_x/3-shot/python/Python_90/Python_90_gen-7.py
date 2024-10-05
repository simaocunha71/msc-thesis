    lst = sorted(set(lst))  # Remove duplicates and sort the list
    if len(lst) < 2:  # If the list has less than 2 elements, return None
        return None
    return lst[1]  # Return the 2nd smallest element


