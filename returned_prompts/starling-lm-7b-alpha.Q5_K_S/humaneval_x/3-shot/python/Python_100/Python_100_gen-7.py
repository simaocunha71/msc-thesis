    result = []
    n_copy = n
    while n_copy > 0:
        if n % 2 == 0:
            result.append(n)
        else:
            result.append(n+1)
        n -= 1
    return result


