    result = [1]
    if n == 0:
        return result
    elif n % 2 == 0:
        result.append(1)
        result.append(n/2)
        for i in range(1, n-1):
            result.append(result[i-1] + result[i])
        return result
    else:
        result.append(result[0] + result[1])
        result.append(result[0] + result[2])
        for i in range(2, n-1):
            result.append(result[i-1] + result[i-2] + result[i+1])
        return result


