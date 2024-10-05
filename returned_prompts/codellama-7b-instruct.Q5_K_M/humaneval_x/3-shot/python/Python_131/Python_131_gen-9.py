    result = 1
    for c in str(n):
        if int(c) % 2 == 1:
            result *= int(c)
    return result

