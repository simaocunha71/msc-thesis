    if not arr:
        return None

    result = 0
    for num in arr:
        if num > 0:
            result += 1
        elif num < 0:
            result -= 1

    return result

