    result = []
    while lst:
        min_val = min(lst)
        max_val = max(lst)
        if min_val == max_val:
            result.extend([min_val] * lst.count(min_val))
            lst = []
        else:
            result.append(min_val)
            lst.remove(min_val)
            result.append(max_val)
            lst.remove(max_val)
    return result

