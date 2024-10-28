    result = []
    for c in music_string:
        if c == ' ':
            continue
        elif c == 'o':
            result.append(4)
        elif c == '|':
            result.append(2)
        elif c == '.':
            result.append(1)

    return result
