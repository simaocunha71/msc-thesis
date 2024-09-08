def second_smallest(lst):
    # Sort the list in ascending order
    sorted_lst = sorted(lst)
    
    # Remove duplicates from the sorted list
    unique_sorted_lst = list(dict.fromkeys(sorted_lst))
    
    # Return the second element in the unique sorted list
    return unique_sorted_lst[1]