    result = []
    for idx, elem in enumerate(l):
        if idx % 2 == 0:
            result.append(sorted(elem)[idx // 2])
        else:
            result.append(elem)
    return result


