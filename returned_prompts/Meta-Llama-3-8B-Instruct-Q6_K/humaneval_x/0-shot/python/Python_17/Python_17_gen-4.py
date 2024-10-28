from typing import List

def parse_music(music_string: str) -> List[int]:
    music = []
    for char in music_string:
        if char == 'o':
            music.append(4)
        elif char == 'o|':
            music.append(2)
        elif char == '.|':
            music.append(1)
    return music

# Test
print(parse_music('o o| .| o| o| .| .| .| .| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
print(parse_music('o o| o| o| o| o| o| o| o| o|'))  # [4, 2, 4, 2, 4, 2, 4, 2, 4, 2]
print(parse_music('.| .| .| .| .| .| .| .| .| .|'))  # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(parse_music('o o o o o o o o o o o'))  # [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
print(parse_music('o| o| o| o| o| o| o| o| o|'))  # [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
print(parse_music('.|.| .|.| .|.| .|.| .|.| .|.|'))  # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(parse_music('.' + '.' + '.' + '.' + '.' + '.' + '.' + '.' + '.' + '.'))  # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(parse_music('.' + '.' + '.' + '.' + '.' + '.' + '.' + '.' + '.' + '.' + '.'))  # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 