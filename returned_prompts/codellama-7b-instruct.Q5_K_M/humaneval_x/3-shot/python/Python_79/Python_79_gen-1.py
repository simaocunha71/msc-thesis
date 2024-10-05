    result = ''

    while decimal > 0:
        result = str(decimal % 2) + result
        decimal //= 2

    return 'db' + result + 'db'

