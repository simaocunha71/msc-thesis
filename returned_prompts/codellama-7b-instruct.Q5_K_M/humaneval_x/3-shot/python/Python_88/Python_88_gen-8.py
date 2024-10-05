    result = array.copy()
    result.sort()
    if sum(result[:2]) % 2 == 0:
        result.reverse()
    return result


