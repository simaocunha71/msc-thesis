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

    note_map = {'.': 1, 'o': 1, 'o|': 2}
    total_beats: List[int] = [0 for _ in range(len(note_string))]

    for i, char in enumerate(music_string):
        if note_map.get(char) is not None:
            total_beats[i] += note_map[char]

    return list(reversed(total_beats))