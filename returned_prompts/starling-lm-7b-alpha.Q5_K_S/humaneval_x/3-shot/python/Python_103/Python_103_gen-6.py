    def get_bin(number: int) -> str:
        return bin(number)[2:]

    if n > m:
        return -1
    elif n == m:
        return get_bin(n)
    else:
        avg = (n + m) / 2
        result = get_bin(round(avg))
        if result[0] == '1':
            result = '0' + result[1:]
        return result


