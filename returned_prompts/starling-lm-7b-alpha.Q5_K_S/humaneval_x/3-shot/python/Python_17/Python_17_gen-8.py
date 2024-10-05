    result = []
    for note in music_string.split('|'):
        if note == 'o':
            result.append(4)
        elif note == 'o|':
            result.append(2)
        else:
            result.append(1)

    return result


