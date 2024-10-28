    even = sorted(l[::2])
    result = []

    for idx, elem in enumerate(l):
        if idx % 2 == 0:
            result.append(even.pop(0))
        else:
            result.append(elem)

    return result

