    result = []
    while decimal:
        if decimal % 2 == 0:
            result.append('0')
        else:
            result.append('1')
        decimal = decimal // 2
    result.reverse()
    return 'db' + ''.join(result) + 'db'


