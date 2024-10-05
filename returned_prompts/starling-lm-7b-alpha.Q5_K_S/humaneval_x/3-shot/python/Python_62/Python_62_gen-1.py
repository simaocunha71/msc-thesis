    if len(xs) == 1:
        return []

    result = []
    for idx, coeff in enumerate(xs):
        if idx == 0:
            if idx + 1 < len(xs):
                result.append(xs[idx + 1])
            else:
                result.append(0)
        else:
            coeff *= idx
            if idx + 1 < len(xs):
                result.append(coeff + xs[idx + 1])
            else:
                result.append(coeff)

    return result[:-1]


