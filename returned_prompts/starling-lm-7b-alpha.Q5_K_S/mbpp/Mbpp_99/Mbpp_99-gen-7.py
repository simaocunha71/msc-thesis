
def decimal_to_binary(n):
    binary = bin(n)[2:]
    return binary.zfill(len(bin(n)[2:]) + 1)


