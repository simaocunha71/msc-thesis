    result = [3]
    current_depth = 0

    for i in range(1, n):
        if i % 2 == 0:
            result.append(1 + i / 2)
        else:
            result.append(result[i - 1] + result[i - 2] + result[i + 1])

    return result

