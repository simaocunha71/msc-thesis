    result = []
    for i, coefficient in enumerate(xs):
        if i == 0:
            result.append(0)
        else:
            result.append(coefficient * (i + 1))
    return result


