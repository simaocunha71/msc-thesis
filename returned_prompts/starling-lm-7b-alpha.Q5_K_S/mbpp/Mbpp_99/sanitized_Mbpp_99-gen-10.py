def decimal_to_binary(n):
    s = ''
    while n:
        s += str(n % 2)
        n //= 2
    return s[::-1]