def pack_consecutive_duplicates(lst):
    result = []
    current = []
    for elem in lst:
        if not current or elem != current[-1]:
            if current:
                result.append(current)
            current = [elem]
        else:
            current.append(elem)
    if current:
        result.append(current)
    return result