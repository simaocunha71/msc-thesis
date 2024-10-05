    result = []
    if a % 2 == 0:
        result.append(a)
    while a < b:
        a += 2
        result.append(a)

    if b % 2 == 0:
        result.append(b)
    while b > a:
        b -= 2
        result.append(b)

    return result


