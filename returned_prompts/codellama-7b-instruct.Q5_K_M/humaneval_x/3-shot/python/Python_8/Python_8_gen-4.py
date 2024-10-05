    result = (0, 1)
    for n in numbers:
        result = (result[0] + n, result[1] * n)

    return result


