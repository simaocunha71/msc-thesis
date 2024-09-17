def check_distinct(tup):
    # Convert tuple to a list
    lst = list(tup)

    # Sort the list to ensure uniqueness
    lst.sort()

    # Check for uniqueness
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            return False
    return True