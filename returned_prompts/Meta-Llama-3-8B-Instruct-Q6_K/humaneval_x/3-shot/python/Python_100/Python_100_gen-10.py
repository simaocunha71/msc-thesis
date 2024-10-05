    result = [n]
    for i in range(n - 1):
        n += 1 if i % 2 else 2
        result.append(n)
    return result


