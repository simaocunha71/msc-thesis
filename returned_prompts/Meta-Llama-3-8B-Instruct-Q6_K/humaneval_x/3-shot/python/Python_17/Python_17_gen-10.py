    result = []
    current_note = ''
    note_duration = {'o': 4, 'o|': 2, '.|': 1}

    for c in music_string:
        if c in note_duration:
            if current_note:
                result.append(note_duration[current_note])
            current_note = c
        elif c == '|':
            result.append(note_duration[current_note])
            current_note = ''

    if current_note:
        result.append(note_duration[current_note])

    return result


