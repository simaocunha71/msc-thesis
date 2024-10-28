    if not lst:
        return []

    sorted_list = sorted(lst)
    result = []
    while sorted_list:
        result.append(sorted_list.pop(0))
        if sorted_list:
            result.append(sorted_list.pop())

    return result


