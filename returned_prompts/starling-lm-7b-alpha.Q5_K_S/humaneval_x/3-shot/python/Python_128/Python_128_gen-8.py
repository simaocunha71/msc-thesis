    if len(arr) == 0:
        return None

    result = 0
    for elem in arr:
        result += abs(elem) * elem // elem

    return result


