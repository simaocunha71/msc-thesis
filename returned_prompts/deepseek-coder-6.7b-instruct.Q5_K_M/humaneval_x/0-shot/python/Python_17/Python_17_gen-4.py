from typing import List

def parse_music(music_string: str) -> List[int]:
    note_duration = {'o': 4, 'o|': 2, '.|': 1}
    notes = music_string.split()
    return [note_duration[note] for note in notes]


print(parse_music('o o| .| o| o| .| .| .| .| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

Explanation:
This solution works by first creating a dictionary that maps the notes to their respective duration. It then splits the input string into a list of notes. The list comprehension then returns a new list where each element is the duration of the corresponding note from the dictionary.

Time complexity: O(n), where n is the number of notes in the input string.
Space complexity: O(n), as a new list is created to store the durations.
"""

# Task 2:

"""
