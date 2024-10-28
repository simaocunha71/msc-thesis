    result = []
    idx = 2
    while n > 1:
        while n % idx != 0:
            idx += 1
        result.append(idx)
        n = n // idx

    return result


