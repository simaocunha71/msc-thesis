    result = []
    for i in range(len(xs)-1):
        result.append(xs[i+1]*i)
    result.append(xs[-1] * len(xs))
    return result


