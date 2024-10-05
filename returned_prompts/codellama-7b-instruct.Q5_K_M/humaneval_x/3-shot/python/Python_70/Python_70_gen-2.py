    result = []
    min_val = min(lst)
    result.append(min_val)
    lst.remove(min_val)
    max_val = max(lst)
    result.append(max_val)
    lst.remove(max_val)
    while len(lst) > 0:
        min_val = min(lst)
        result.append(min_val)
        lst.remove(min_val)

    return result


