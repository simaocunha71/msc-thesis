    result = ""
    while N:
        result += str(N % 2)
        N //= 2
    result = result[::-1]
    return result


