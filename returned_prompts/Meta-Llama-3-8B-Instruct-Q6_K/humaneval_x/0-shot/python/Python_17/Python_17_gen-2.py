from typing import List

def parse_music(music_string: str) -> List[int]:
    music_list = music_string.split()
    beat_list = []
    for note in music_list:
        if note == 'o':
            beat_list.append(4)
        elif note == 'o|':
            beat_list.append(2)
        elif note == '.|':
            beat_list.append(1)
    return beat_list

print(parse_music('o o| .| o| o| .| .| .| .| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]  # 4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]  # 4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]  # 4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]  # 4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]  # 4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]  # 4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]  # 4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]  # 4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]  # 4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]  # 4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]  # 4, 2, 1, 2, 2, 1, 1