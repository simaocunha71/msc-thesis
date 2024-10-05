    result = []

    i = 2
    while n > 1:
        if n % i == 0:
            result.append(i)
            n = n // i
        else:
            i += 1

    return result

