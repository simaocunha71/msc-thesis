    words = s.split(' ')
    result = []

    for word in words:
        chars = list(word)
        chars.sort(key=lambda x: ord(x))
        result.append(''.join(chars))

    return ' '.join(result)


