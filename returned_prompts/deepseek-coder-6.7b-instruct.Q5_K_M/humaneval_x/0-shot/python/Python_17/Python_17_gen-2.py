from typing import List


def parse_music(music_string: str) -> List[int]:
    music_list = music_string.split()
    beats_list = []
    for note in music_list:
        if note == 'o':
            beats_list.append(4)
        elif note == 'o|':
            beats_list.append(2)
        elif note == '.|':
            beats_list.append(1)
    return beats_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()


In the function `parse_music`, we split the input string `music_string` into a list of strings `music_list` using `.split()`. Then, we iterate over `music_list`, check each note and append the corresponding number of beats to `beats_list`. Finally, we return `beats_list`.

Note: If you have a string where there are white spaces in between the notes and you want to remove them, you can add `.replace(' ', '')` before `.split()`.

This function will work as long as the input string is well-formed and contains only the characters 'o', 'o|', and '.|'. If the input string contains other characters, the function will not work correctly.

Also, it assumes that there is no other character in the string apart from 'o', 'o|', and '.|'. If there are other characters, they will be ignored.
"""

from typing import List


def parse_music(music_string: str) -> List[int]:
    music_list = music_string.replace(' ', '').split()
    beats_list = []
    for note in music_list:
        if note == 'o':
            beats_list.append(4)
        elif note == 'o|':
            beats_list.append(2)
        elif note == '.|':
            beats_list.append(1)
    return beats_list


if __name__ == "__main__":
    import doctest
   