def maximize_elements(t1, t2):
    result = []
    for x, y in zip(t1, t2):
        if x[0] > y[0]:
            result.append(x)
        elif x[0] < y[0]:
            result.append(y)
        else:
            if x[1] > y[1]:
                result.append(x)
            else:
                result.append(y)
    return tuple(result)