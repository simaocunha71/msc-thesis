    result = []
    stones = 0
    for i in range(n):
        if n % 2 == 0:
            stones += n + 2*i
        else:
            stones += n + 2*i
        result.append(stones)
    return result


