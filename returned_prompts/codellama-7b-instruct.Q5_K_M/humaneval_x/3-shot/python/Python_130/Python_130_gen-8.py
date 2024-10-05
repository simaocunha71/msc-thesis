    result = [1, 3]
    a = 1
    b = 3
    c = 2
    for i in range(2, n + 1):
        if i % 2 == 0:
            result.append(int((c + i / 2) % (1e9 + 7)))
        else:
            result.append(a + b + c)
            a = b
            b = c
            c = result[-1]
    return result


