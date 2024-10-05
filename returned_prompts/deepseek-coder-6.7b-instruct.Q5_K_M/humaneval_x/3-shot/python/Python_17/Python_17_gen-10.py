    result = []
    for c in music_string.split():
        if c == 'o':
            result.append(4)
        elif c == 'o|':
            result.append(2)
        elif c == '.|':
            result.append(1)

    return result


