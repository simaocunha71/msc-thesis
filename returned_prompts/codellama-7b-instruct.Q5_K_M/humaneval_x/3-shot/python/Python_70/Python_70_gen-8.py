    result = []

    if not lst:
        return result

    min_value = min(lst)
    max_value = max(lst)

    while min_value <= max_value:
        result.append(min_value)
        lst.remove(min_value)
        max_value = max(lst)
        result.append(max_value)
        lst.remove(max_value)
        min_value = min(lst)

    return result


