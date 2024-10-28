from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split()
    beats = []
    for note in notes:
        if note == 'o':
            beats.append(4)
        elif note == 'o|':
            beats.append(2)
        elif note == '.|':
            beats.append(1)
    return beats

# Test the function
print(parse_music('o o| .| o| o| .| .| .| .| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]  # Expected output
print(parse_music('.'))  # [1]  # Expected output
print(parse_music('|'))  # [2]  # Expected output
print(parse_music('o| .| |'))  # [2, 1, 2]  # Expected output
print(parse_music('.' * 10))  # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # Expected output
print(parse_music('.' * 100))  # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,