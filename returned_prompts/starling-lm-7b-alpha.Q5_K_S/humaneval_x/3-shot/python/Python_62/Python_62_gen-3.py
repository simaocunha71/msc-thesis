    result = []
    for idx, elem in enumerate(xs):
        if idx == 0:
            result.append(0)
        elif idx == 1:
            result.append(elem * idx)
        else:
            result.append(elem * idx)
            result[-2] += elem

    return result


