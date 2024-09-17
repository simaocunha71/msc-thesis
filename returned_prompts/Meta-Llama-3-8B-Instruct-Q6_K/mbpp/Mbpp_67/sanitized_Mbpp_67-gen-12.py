def bell_number(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        result = 0
        for i in range(n + 1):
            result += ((-1) ** i) * math.comb(n, i) * bell_number(i)
        return result