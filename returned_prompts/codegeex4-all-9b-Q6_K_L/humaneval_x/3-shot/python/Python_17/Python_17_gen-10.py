    result = []
    beats = 0

    for c in music_string:
        if c == 'o':
            beats += 4
            result.append(beats)
        elif c == 'o|':
            beats += 2
            result.append(beats)
        elif c == '.|':
            beats += 1
            result.append(beats)

    return result

