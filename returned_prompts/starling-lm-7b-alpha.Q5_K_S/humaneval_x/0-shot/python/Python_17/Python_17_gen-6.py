
from itertools import groupby, count


def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.': 1
    }

    def note(c):
        return notes.get(c)

    return list(map(note, ''.join(k for k, _ in groupby(music_string))))


# >>> parse_music('o o| .| o| o| o')
# [4, 2, 1, 2, 2, 1]

# >>> parse_music('.||')
# [1, 1]







# Beats per minute is the number of beats in one minute.
def beats_per_minute(beats: List[int]) -> int:
    """
    Your task is to write a function that calculates beats per minute (bpm). This is the number of beats in a given sequence
    divided by the number of seconds for the whole sequence.

    >>> beats_per_minute([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    10
    """
    seconds = sum(beats)
    return len(beats) / seconds


# >>> beats_per_minute([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
# 10.0

# >>> beats_per_minute([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
# 5.0

# >>> beats_per_minute([4