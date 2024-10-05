    result = []
    current_beat = 0

    for c in music_string.split():
        if c == 'o':
            current_beat = 4
        elif c == 'o|':
            current_beat = 2
        elif c == '.|':
            current_beat = 1

        result.append(current_beat)

    return result

