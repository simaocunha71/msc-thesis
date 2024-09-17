def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    while len(binary) < 4:
        binary = '0' + binary
    return binary