    result = [n]
    i = 1
    while n > 1:
        if n % 2 == 1:
            n = n - i
            result.append(n + i + 1)
            i += 2
        else:
            n = n - i
            result.append(n + i)
            i += 2
    return result


