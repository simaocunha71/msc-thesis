def maximize_elements(tuple1, tuple2):
    result = []
    for a, b in zip(tuple1, tuple2):
        if a[0] > b[0]:
            result.append(a)
        elif a[0] < b[0]:
            result.append(b)
        else:
            if a[1] > b[1]:
                result.append(a)
            else:
                result.append(b)
    return tuple(result)