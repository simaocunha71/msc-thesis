def find_Parity(n):
    binary = bin(n)[2:]
    return binary.count('1') % 2 != 0