from typing import List


def parse_music(music_string: str) -> List[int]:
    music_list = music_string.split()
    result = []
    for note in music_list:
        if note == 'o':
            result.append(4)
        elif note == 'o|':
            result.append(2)
        elif note == '.|':
            result.append(1)
    return result


print(parse_music('o o| .| o| o| .| .| .| .| o o'))

#  Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]


# This solution works by first splitting the input string into a list of notes. It then iterates over each note and appends the corresponding number of beats to the result list. Finally, it returns the result list.

# This solution assumes that the input string is correctly formatted, with no invalid characters. If this is not the case, you would need to add error checking to handle such inputs.

# The time complexity of this solution is O(n), where n is the number of notes in the input string. This is because it makes a single pass over the input string. The space complexity is also O(n), as it creates a new list to store the result.

# Please note that the input string is split by spaces. If the notes are separated by other characters, you would need to adjust the split function accordingly.

# Also, this solution assumes that all valid notes are represented with the exact same strings as in the question. If this is not the case, you would need to add a mapping from strings to integers to handle such notes.

# Finally, this solution assumes that all notes have valid durations. If this is not the case, you would need to add error checking to handle such notes.

# Overall, this solution should work for the given problem, but you may need to adjust it based on the specifics of your task.


#  This solution works by first splitting the input string into a list of notes. It then iterates over each note and appends the corresponding number of beats to the result list. Finally, it returns the result list