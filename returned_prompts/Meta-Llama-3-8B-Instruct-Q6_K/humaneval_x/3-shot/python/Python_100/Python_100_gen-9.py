    result = [n]
    n += 1

    while n <= 10:
        if n % 2 == 1:
            n += 1
        else:
            n += 2
        result.append(n)

    return result


