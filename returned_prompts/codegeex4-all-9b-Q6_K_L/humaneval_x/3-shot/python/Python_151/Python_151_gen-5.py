    result = 0
    for n in lst:
        if n % 2 == 1 and n >= 0:
            result += n ** 2
    return result

