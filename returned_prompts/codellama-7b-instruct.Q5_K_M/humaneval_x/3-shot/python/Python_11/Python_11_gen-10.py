    result = ''

    for i in range(len(a)):
        if a[i] != b[i]:
            result += '1'
        else:
            result += '0'

    return result


