    music_notes = music_string.split()

    beat_values = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    return [beat_values[note] for note in music_notes]


