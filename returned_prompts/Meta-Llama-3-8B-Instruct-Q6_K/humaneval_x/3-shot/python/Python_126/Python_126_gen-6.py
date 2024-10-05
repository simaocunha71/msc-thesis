    return len(set(lst)) == len(lst) and lst == sorted(lst)
    # The set function removes duplicates, so if the lengths are equal, there were no duplicates
    # The sorted function checks if the list is in ascending order


