    result = []
    current_beats = 0

    for c in music_string:
        if c == 'o':
            current_beats = 4
        elif c == 'o|':
            current_beats = 2
        elif c == '.|':
            current_beats = 1

        result.append(current_beats)

    return result

