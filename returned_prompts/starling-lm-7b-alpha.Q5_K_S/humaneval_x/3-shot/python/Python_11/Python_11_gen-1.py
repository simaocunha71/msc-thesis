    result = ""
    for i in range(len(a)):
        if a[i] == '1' and b[i] == '1':
            result += '0'
        elif (a[i] == '0' and b[i] == '0') or (a[i] == '1' and b[i] == '0') or (a[i] == '0' and b[i] == '1'):
            result += '1'
    return result


