    result = []
    music_notes = music_string.split()

    for note in music_notes:
        if note == 'o':
            result.append(4)
        elif note == 'o|':
            result.append(2)
        elif note == '.|':
            result.append(1)

    return result


