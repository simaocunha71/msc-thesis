    result = ''
    while s:
        result += s[:3][1:] + s[:3][0]
        s = s[3:]
    return result


