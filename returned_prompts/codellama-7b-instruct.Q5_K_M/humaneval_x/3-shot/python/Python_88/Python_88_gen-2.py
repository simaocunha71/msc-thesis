    result = array.copy()
    result.sort()

    if sum(result[0], result[-1]) % 2 == 0:
        result.reverse()

    return result


