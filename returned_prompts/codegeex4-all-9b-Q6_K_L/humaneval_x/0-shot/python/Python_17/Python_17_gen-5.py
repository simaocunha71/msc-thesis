```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    # Initialize an empty list to store the lengths of the notes
    note_lengths = []

    # Split the input string into a list of notes
    notes = music_string.split()

    # Iterate over each note in the list
    for note in notes:
        # Check the length of the note
        if note == 'o':
            note_lengths.append(4)
        elif note == 'o|':
            note_lengths.append(2)
        elif note == '.|':
            note_lengths.append(1)

    # Return the list of note lengths
    return note_lengths

# Test the function
print(parse_music('o o| .| o| o| .| .| .| .| o o'))
```
