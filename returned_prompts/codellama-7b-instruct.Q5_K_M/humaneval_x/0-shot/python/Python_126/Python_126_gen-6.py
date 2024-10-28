
    # Sort and compare
    return sorted(lst) == lst

    # or

    # Sort and check if the same
    return sorted(lst) == lst

    # or

    # Check for duplicates and if the list is sorted
    return not lst.count(lst[0]) < len(lst) - 1 and lst == sorted(lst)

    # or

    # Check for duplicates and if the list is sorted
    return lst.count(lst[0]) < len(lst) - 1 and lst == sorted(lst)

    # or

    # Check if all the elements in the list are sorted
    return all(i <= j for i, j in zip(lst, lst[1:]))

    # or

    # Check if the list is sorted and has no duplicates
    return lst == sorted(lst) and len(lst) == len(set(lst))
