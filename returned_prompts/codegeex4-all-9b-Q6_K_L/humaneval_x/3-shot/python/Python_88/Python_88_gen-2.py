    copy = array.copy()
    sum = copy[0] + copy[-1]

    if sum % 2 == 0:
        copy.sort(reverse=True)
    else:
        copy.sort()

    return copy

