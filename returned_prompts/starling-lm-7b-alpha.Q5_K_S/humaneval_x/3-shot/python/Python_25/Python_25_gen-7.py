    result = []
    i = 2
    while n > 1:
        while n % i == 0:
            n //= i
            result.append(i)
        i += 1
    return result


