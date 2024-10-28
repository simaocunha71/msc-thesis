    result = 0
    for c in s:
        if 'A' <= c <= 'Z':
            result += ord(c) - ord('A') + 1
    return result


