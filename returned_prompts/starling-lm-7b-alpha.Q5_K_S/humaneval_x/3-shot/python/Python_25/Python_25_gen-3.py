    result = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            result.append(i)
            n //= i
        i += 1

    if n > 1:
        result.append(n)

    return result


