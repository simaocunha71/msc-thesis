    result = 0
    for i in lst:
        if i < 0:
            i = -i
        result += i ** 2
    return result


