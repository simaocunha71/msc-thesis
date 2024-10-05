    if not arr:
        return None

    signs = [1, -1, 1]
    result = 0
    product = 1

    for num in arr:
        product *= signs[num]
        result += abs(num) * product

    return result


