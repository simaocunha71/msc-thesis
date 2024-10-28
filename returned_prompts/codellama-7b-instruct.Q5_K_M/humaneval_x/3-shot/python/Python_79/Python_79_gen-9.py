    binary = ''
    while decimal != 0:
        if decimal % 2 == 0:
            binary = '0' + binary
        else:
            binary = '1' + binary
        decimal = decimal // 2
    return 'db' + binary + 'db'


