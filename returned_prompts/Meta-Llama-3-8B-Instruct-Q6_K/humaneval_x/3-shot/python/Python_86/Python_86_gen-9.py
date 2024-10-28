    words = s.split()
    result = []
    for word in words:
        result.append(''.join(sorted(word)))
    return ' '.join(result)


