    result = []
    for c in music_string:
        if c == 'o':
            result.append(4)
        elif c == '.':
            result.append(1)
        elif c == '|':
            result.append(0)

    return result


