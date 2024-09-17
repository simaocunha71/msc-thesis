def decimal_to_binary(n):
    if n == 0:
        return '0'
    binary_number = ''
    while n > 0:
        binary_number = str(n % 2) + binary_number
        n //= 2
    return binary_number