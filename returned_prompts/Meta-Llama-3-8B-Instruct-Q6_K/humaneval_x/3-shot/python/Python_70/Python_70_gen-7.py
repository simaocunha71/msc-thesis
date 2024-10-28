    if not lst:
        return []
    min_val = min(lst)
    max_val = max(lst)
    result = [min_val]
    lst.remove(min_val)
    while lst:
        max_val = max(lst)
        result.append(max_val)
        lst.remove(max_val)
        if lst:
            min_val = min(lst)
            result.append(min_val)
            lst.remove(min_val)
    return result


