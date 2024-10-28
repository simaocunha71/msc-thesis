    if n == 0:
        return [1]
    elif n == 1:
        return [1, 3]
    elif n == 2:
        return [1, 3, 2]
    else:
        result = [1, 3, 2]
        for i in range(3, n + 1):
            result.append(result[i - 1] + result[i - 2] + result[i - 3])
        return result

