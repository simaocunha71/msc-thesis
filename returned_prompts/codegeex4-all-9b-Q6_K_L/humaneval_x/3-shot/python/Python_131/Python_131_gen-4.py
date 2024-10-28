    result = 1
    for d in str(n):
        if int(d) % 2 == 1:
            result *= int(d)
    return result

