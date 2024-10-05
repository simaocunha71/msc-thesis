
    # Check the length of the list
    if len(l) < 2:
        return True

    # Check the increasing or decreasing
    if l[1] < l[0]:
        for i in range(2, len(l)):
            if l[i] < l[i-1]:
                return False
    else:
        for i in range(2, len(l)):
            if l[i] > l[i-1]:
                return False

    return True
