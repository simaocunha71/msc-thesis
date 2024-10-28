def decimal_to_binary(n):
    if n == 0:
        return '0'
    binary = ''
    while n:
        binary = str(n % 2) + binary
        n //= 2
    return binary