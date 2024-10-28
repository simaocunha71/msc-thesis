    result = []
    count = 0
    for c in text:
        if c == ' ':
            if count == 1:
                result.append('-')
            else:
                result.append('_')
                count += 1
        else:
            result.append(c)
            count = 0
    return ''.join(result)


