    beats_per_note = {'o': 4, 'o|': 2, '.|': 1}
    return [beats_per_note[note] for note in music_string.split()]


