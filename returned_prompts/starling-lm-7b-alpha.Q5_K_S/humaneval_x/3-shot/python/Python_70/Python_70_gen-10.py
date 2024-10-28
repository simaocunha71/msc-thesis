    result = []
    while len(lst) > 0:
        min_value = min(lst)
        result.append(min_value)
        lst.remove(min_value)
        if len(lst) == 0:
            break
        max_value = max(lst)
        result.append(max_value)
        lst.remove(max_value)
    return result


