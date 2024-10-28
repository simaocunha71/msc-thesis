    result = [0, 1]

    for num in numbers:
        result[0] += num
        result[1] *= num

    return tuple(result)


