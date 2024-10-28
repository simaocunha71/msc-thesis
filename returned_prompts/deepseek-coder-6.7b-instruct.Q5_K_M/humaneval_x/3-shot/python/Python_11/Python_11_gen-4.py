    result = []

    for i in range(len(a)):
        result.append(str(int(a[i]) ^ int(b[i])))

    return ''.join(result)


