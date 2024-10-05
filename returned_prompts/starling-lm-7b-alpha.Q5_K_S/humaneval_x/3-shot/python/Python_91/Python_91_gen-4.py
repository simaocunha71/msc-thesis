    result = 0
    current = ''
    for c in S:
        if c == '.' or c == '?' or c == '!':
            if current.startswith('I'):
                result += 1
            current = ''
        else:
            current += c
    return result


