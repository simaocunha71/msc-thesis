from typing import List

def parse_music(music_string: str) -> List[int]:
    result = []
    i = 0
    while i < len(music_string):
        if music_string[i] == 'o':
            result.append(4)
            i += 1
        elif music_string[i:i+2] == 'o|':
            result.append(2)
            i += 2
        elif music_string[i:i+3] == '.| ':
            result.append(1)
            i += 3
        else:
            raise ValueError("Invalid music string")
    return result

# Test
print(parse_music('o o| .| o| o| .| .| .| .| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
print(parse_music('o| .|| o| o| o|'))  # [2, 1, 2, 2, 1, 2, 2]
print(parse_music('o| o| o| o|'))  # [2, 2, 2, 2]





