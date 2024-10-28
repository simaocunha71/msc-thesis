    result = []
    current_beat = 0

    for c in music_string:
        if c == 'o':
            current_beat += 4
            result.append(current_beat)
        elif c == 'o|':
            current_beat += 2
            result.append(current_beat)
        elif c == '.|':
            current_beat += 1
            result.append(current_beat)

    return result

