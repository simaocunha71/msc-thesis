    result = [0] * len(xs)
    for i in range(1, len(xs)):
        result[i] = xs[i - 1] * i
    return result


