    if len(arr) == 0:
        return None
    result = 0
    for elem in arr:
        if elem < 0:
            elem = elem * -1
            result *= -1
        result += elem
    return result


