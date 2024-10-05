    if n == 0:
        return [3]
    elif n == 1:
        return [3]
    elif n == 2:
        return [3, 2]
    else:
        result = [3, 2]
        for i in range(2, n):
            if i % 2 == 0:
                result.append(1 + i / 2)
            else:
                a, b = result[-2], result[-1]
                result.append(a + b + 1)
        return result
    return result


