    result = [0] * len(xs)

    for idx, x in enumerate(xs):
        if idx == 0:
            continue
        result[idx - 1] = idx * x

    return result


