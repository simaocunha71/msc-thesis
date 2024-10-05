    result = []
    for i in range(len(xs)-1):
        result.append(xs[i+1] * (i+1))
    result.append(xs[0])
    return result


