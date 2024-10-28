    result = 0
    for num in lst:
        if num < 0 or not isinstance(num, int):
            continue
        else:
            result += num ** 2
    return result


