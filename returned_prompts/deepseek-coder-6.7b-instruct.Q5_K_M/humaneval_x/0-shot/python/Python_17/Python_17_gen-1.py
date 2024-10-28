```python
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

print(parse_music('o o| .| o| o| .| .| .| .| o o')) # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This function splits the input string into a list of strings, where each string is a single note. Then it iterates over each note, checks what it is, and appends the corresponding number of beats to the result list. Finally, it returns the result list.

It's important to note that the input string is assumed to be well-formatted, with no validation. If the input string could have errors, the function would need to be updated to handle those cases.

The function also assumes that the input string represents a single piece of music, with each note separated by a space. If the input string represents multiple pieces of music, the function would need to be updated to handle that case.

If the input string is in a different format, the function would need to be updated to handle that format.

Finally, the function assumes that the input string represents musical notes in a special ASCII format. If the input string represents notes in a different format, the function would need to be updated to handle that format.

This function is case-sensitive, so it will not recognize 'O', 'O|', '.|', etc. as valid notes.
"""
```

