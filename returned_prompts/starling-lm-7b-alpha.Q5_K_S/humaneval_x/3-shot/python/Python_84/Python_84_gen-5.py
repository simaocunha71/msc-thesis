    result = []
    while N != 0:
        result.append(str(N % 2))
        N = N // 2
    return "".join(result[::-1])


