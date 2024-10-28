def parse_music(music_string: str) -> List[int]:
    beats = []
    notes = music_string.split()
    for note in notes:
        if note == 'o':
            beats.append(4)
        elif note == 'o|':
            beats.append(2)
        elif note == '.|':
            beats.append(1)
    return beats


print(parse_music('o o| .| o| o| .| .| .| .| o o'))

# Test cases
assert parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
assert parse_music('o o| o| .| .| .| o| .| o| o| o| .| .| .| .| .| o o') == [4, 2, 2, 1, 1, 2, 1, 2, 2, 1, 1, 1, 1, 4, 2, 2, 1, 1]

The code works by iterating over the notes in the music string and adding the corresponding number of beats to the beats list. It splits the string by spaces to get each note.
"""

# Test cases
assert parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
assert parse_music('o o| o| .| .| .| o| .| o| o| o| .| .| .| .| .| o o') == [4, 2, 2, 1, 1, 2, 1, 2, 2, 1, 1, 1, 1, 4, 2, 2, 1, 1]
<jupyter_output>
<empty_output>
