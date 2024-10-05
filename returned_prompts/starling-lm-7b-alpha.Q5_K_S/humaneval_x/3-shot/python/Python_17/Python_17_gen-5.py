    result = []
    current_beats = 0

    for c in music_string:
        if c == 'o':
            result.append(4)
            current_beats += 4
        elif c == 'o|':
            result.append(2)
            current_beats += 2
        elif c == '.':
            result.append(1)
            current_beats += 1

    return result


