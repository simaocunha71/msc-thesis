    if n > m:
        return -1

    avg = (n + m) / 2
    if avg % 1 == 0:
        result = str(bin(avg))
    else:
        result = str(bin(avg // 1)) + "1"

    result = '0b' + result[2:]

    return result


