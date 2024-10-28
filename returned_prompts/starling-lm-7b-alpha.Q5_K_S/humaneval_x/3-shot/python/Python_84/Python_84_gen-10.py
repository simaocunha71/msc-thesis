    result = []
    while N:
        result.append(str(N % 2))
        N = N // 2
    return "".join(result[::-1])


