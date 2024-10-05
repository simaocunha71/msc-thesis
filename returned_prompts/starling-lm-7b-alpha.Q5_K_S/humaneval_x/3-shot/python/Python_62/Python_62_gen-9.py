    result = []
    for idx, coef in enumerate(xs):
        if idx == 0:
            result.append(0)
        elif idx == 1:
            result.append(coef * idx)
        else:
            result.append(coef * idx)
            result[-2] += coef * idx

    return result


