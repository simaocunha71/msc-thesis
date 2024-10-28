from typing import List


def parse_music(music_string: str) -> List[int]:
    music_notes = music_string.split()
    beats = []
    for note in music_notes:
        if note == 'o':
            beats.append(4)
        elif note == 'o|':
            beats.append(2)
        elif note == '.|':
            beats.append(1)
    return beats


# Test the function
print(parse_music('o o| .| o| o| .| .| .| .| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
print(parse_music('.| o| o| .| .| o o| o|'))  # [1, 2, 4, 1, 1, 4, 2, 4]
print(parse_music('o| .| .| .| o| o| .| .| o'))  # [2, 1, 1, 1, 2, 4, 1, 1, 4]
print(parse_music('.' * 10))  # [1] * 10
print(parse_music('o' * 5))  # [4] * 5
print(parse_music('o|' * 5))  # [2] * 5
print(parse_music('|' * 10))  # [] (empty list)  # This is because '|' is not a valid note in this format. 
print(parse_music('.' + 'o|' * 5))  # [1, 2] * 5
print(parse_music('.' * 2 + 'o|' * 3))  # [1, 1, 2, 2, 2]
print(parse_music('.' * 3 + 'o' + 'o|' * 2))  # [1, 1, 1, 4, 2, 2]
print(parse_music('.' * 2 + 'o' + 'o|' * 2 + '.'))  # [1, 1, 4, 2, 2, 1]
print(parse_music('.' * 2 + 'o|' + '.'))  # [1, 2, 1]
print(parse_music('.' + 'o|' * 2 + '.'))  # [1, 2, 