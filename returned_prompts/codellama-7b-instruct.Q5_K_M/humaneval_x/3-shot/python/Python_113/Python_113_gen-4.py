    result = []

    for s in lst:
        result.append(str(sum(int(c) % 2 == 1 for c in s)))

    return result


