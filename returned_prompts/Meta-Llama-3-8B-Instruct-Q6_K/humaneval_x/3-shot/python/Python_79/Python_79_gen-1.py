    binary = bin(decimal)[2:]
    return 'db' + '0' * (8 - len(binary)) + binary + 'db'


