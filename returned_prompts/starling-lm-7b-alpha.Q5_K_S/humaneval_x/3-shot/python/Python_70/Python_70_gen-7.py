    result = []
    while len(lst) > 0:
        result.append(min(lst))
        lst.remove(min(lst))
        if len(lst) > 0:
            result.append(max(lst))
            lst.remove(max(lst))
    return result


