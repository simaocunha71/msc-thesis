    result = []
    while lst:
        min_val = min(lst)
        result.append(min_val)
        lst.remove(min_val)
        if len(lst) == 0:
            break
        max_val = max(lst)
        result.append(max_val)
        lst.remove(max_val)
    return result


