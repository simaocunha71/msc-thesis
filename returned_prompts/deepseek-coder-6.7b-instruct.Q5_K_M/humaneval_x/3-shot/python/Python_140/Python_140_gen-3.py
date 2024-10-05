    result = []
    count = 0
    for c in text:
        if c == ' ':
            count += 1
            if count == 2:
                result.append('_')
            elif count > 2:
                result[-1] = '-'
        else:
            if count > 1:
                result.append('_')
            result.append(c)
            count = 0
    return ''.join(result)


