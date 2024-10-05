    result = []
    count = n
    while count > 0:
        result.append(count)
        count += 1 if n % 2 == 1 else 2
        n -= 1
    return result


