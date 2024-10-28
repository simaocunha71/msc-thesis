    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:  # if i is even
            result.append(math.factorial(i))
        else:  # if i is odd
            result.append(sum(range(1, i + 1)))
    return result


