    result = []
    while lst:
        result.append(min(lst))
        lst.remove(min(lst))
        if lst:
            result.append(max(lst))
            lst.remove(max(lst))

    return result

