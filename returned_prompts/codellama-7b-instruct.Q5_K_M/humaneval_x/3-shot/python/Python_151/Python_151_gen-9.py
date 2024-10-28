    result = 0
    for element in lst:
        if element > 0 and element % 2 == 1:
            result += element ** 2
    return result


