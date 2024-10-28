def decimal_to_binary(n):
    res = []
    while n > 0:
        res.append(str(n % 2))
        n = n // 2
    return "".join(res[::-1])