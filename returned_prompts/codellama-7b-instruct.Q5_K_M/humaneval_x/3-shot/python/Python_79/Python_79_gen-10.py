    binary = []
    for i in range(32):
        if (decimal >> i) & 1:
            binary.append('1')
        else:
            binary.append('0')

    return 'db' + ''.join(binary) + 'db'


