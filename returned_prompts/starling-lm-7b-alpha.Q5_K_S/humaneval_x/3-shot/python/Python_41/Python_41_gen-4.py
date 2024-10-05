    result = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if abs(i - j) == 1:
                result += 1
    return result


