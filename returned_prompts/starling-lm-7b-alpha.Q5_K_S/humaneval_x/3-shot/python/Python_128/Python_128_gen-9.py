    if len(arr) == 0:
        return None
    result = 1
    for elem in arr:
        if elem == 0:
            result *= 0
        elif elem < 0:
            result *= -1
        else:
            result *= 1
    return abs(result)


