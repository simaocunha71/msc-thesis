    result = []
    for idx, elem in enumerate(l):
        if idx % 3:
            result.append(elem)
        else:
            result.append(sorted([elem] + result[idx//3::]))[0]
    return result


