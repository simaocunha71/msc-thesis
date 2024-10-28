    notes = music_string.split()
    beats = [0] * len(notes)
    for i, note in enumerate(notes):
        if note == 'o':
            beats[i] = 4
        elif note == 'o|':
            beats[i] = 2
        elif note == '.|':
            beats[i] = 1
        else:
            raise Exception(f'Invalid note: {note}')
    return beats