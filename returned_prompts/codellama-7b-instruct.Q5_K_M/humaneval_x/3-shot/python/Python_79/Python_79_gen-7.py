    binary = ''
    for i in range(16):
        if decimal == 0:
            break
        if decimal % 2 == 1:
            binary = '1' + binary
        else:
            binary = '0' + binary
        decimal = decimal >> 1
    return 'db' + binary + 'db'
