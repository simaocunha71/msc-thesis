    result = [n]

    while sum(result) < n:
        result.append(result[-1] + 2)

    return result

