
def decimal_to_binary(n):
    binary = bin(n)[2:]
    if len(binary) < 4:
        return '0' * (4 - len(binary)) + binary
    else:
        return binary


