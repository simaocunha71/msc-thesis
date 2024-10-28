    if N == 0:
        return "0"

    result = ""
    while N > 0:
        result += str(N % 2)
        N //= 2

    return str(int(result, 2))


