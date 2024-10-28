    result = []
    min_val = min(lst)
    max_val = max(lst)
    while min_val in lst or max_val in lst:
        result.append(min_val)
        lst.remove(min_val)
        min_val = min(lst)
        if max_val in lst:
            result.append(max_val)
            lst.remove(max_val)
            max_val = max(lst)
    return result


