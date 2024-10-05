    result = 0
    for num in lst:
        if num % 2 != 0 and num >= 0 and num % 1 == 0:
            result += num ** 2
    return result


