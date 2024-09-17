def decimal_to_binary(n):
    bin_str = ''
    while n > 0:
        bin_str += str(n % 2)
        n //= 2
    return bin_str[::-1]