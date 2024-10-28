    result = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            result.append(i)
    if n > 1:
        result.append(n)
    return result


