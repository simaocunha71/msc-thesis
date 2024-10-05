    result = []
    while lst:
        min_elem = min(lst)
        result.append(min_elem)
        lst.remove(min_elem)
        if lst:
            max_elem = max(lst)
            result.append(max_elem)
            lst.remove(max_elem)

    return result


