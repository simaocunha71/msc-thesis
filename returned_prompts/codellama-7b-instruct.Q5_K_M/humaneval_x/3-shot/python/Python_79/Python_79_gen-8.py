    binary = ''

    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2

    return 'db' + binary + 'db'


