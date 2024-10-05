    result = [n]
    for i in range(1, n):
        if result[i-1] % 2 == 0:
            result.append(result[i-1] + 2)
        else:
            result.append(result[i-1] + 2)
    return result


