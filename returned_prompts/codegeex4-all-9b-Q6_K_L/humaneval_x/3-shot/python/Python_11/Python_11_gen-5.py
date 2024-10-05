    result = ''
    for idx, _ in enumerate(a):
        if a[idx] == b[idx]:
            result += '0'
        else:
            result += '1'

    return result


