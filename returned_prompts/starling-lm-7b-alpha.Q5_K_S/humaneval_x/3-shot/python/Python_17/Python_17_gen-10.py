    result = []
    current_duration = 0

    for c in music_string:
        if c == 'o':
            result.append(4)
        elif c == '.':
            result.append(1)
        elif c == '|':
            current_duration += 1

    return result


