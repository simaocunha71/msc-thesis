    result = []
    note_lengths = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    for note in music_string.split(' '):
        if note:
            result.append(note_lengths[note])

    return result

