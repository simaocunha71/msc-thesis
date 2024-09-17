def pack_consecutive_duplicates(lst):
    result = []
    current = []
    for i in lst:
        if not current or i != current[-1]:
            if current:
                result.append(current)
            current = [i]
        else:
            current.append(i)
    if current:
        result.append(current)
    return result