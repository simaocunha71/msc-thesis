    music_string = music_string.replace(' ', '')  # Remove spaces
    result = []
    for note in music_string.split('|'):
        if note == 'o':
            result.append(4)
        elif note == 'o|':
            result.append(2)
        elif note == '.|':
            result.append(1)

    return result
    # Alternatively, you can use a dictionary for mapping notes to their lengths
    # notes = {'o': 4, 'o|': 2, '.|': 1}
    # return [notes[note] for note in music_string.split('|')]


