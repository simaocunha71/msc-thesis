def maximize_elements(t1, t2):
    result = []
    for a, b in zip(t1, t2):
        if a[1] > b[1]:
            result.append(a)
        elif a[1] < b[1]:
            result.append(b)
        else:
            if a[0] < b[0]:
                result.append(a)
            else:
                result.append(b)
    return tuple(result)