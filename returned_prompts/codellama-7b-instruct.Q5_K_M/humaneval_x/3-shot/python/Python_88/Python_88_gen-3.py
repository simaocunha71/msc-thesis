    result = array[:]
    result.sort()

    if sum(result) % 2 == 0:
        result.reverse()

    return result


