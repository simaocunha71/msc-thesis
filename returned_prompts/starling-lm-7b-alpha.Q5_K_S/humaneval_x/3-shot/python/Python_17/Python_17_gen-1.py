    result = []
    current_note = ''
    for c in music_string:
        if c == 'o' or c == 'o|':
            result.append(4)
        elif c == '.':
            result.append(1)
        current_note += c

    return result


