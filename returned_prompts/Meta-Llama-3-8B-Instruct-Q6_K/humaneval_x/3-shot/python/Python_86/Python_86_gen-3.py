    words = s.split()
    result = []
    for word in words:
        result.append(''.join(sorted(word)))
    return ' '.join(result)  # join words with space in between


