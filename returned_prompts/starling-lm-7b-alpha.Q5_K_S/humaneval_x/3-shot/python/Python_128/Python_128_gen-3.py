    if len(arr) == 0:
        return None
    result = 0
    for i in arr:
        if i < 0:
            result -= i
        else:
            result += i
    return result


