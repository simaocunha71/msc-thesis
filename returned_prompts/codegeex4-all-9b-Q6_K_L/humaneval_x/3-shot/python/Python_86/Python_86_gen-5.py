    words = s.split()
    result = ''
    for word in words:
        result += ''.join(sorted(word)) + ' '
    return result.strip()

