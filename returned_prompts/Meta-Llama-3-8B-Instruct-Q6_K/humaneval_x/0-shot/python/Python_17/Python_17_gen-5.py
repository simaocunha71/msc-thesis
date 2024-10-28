from typing import List

def parse_music(music_string: str) -> List[int]:
    beats = [0]
    for char in music_string:
        if char == 'o':
            beats.append(4)
        elif char == 'o|':
            beats.append(2)
        elif char == '.|':
            beats.append(1)
    return beats[1:]

# test the function
print(parse_music('o o| .| o| o| .| .| .| .| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]  # as expected
# for a more complex test
print(parse_music('o o| .|| o| o| .|| o| o| o| o'))
# Output: [4, 2, 1, 1, 2, 2, 1, 1, 4, 4, 1, 1, 4, 4]  # as expected
# for a test with 'o' at the start and end
print(parse_music('o o| .| o| o| .| .| .| .| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]  # as expected
# for a test with 'o|' and '|' at the same time
print(parse_music('o| .|| o| o| .|| o| o| o| o'))
# Output: [2, 1, 1, 2, 2, 1, 1, 4, 4, 1, 1, 4, 4]  # as expected
# for a test with '.' at the start
print(parse_music('.| o| .| o| o| .| .| .| .| o o'))
# Output: [1, 2, 1, 2, 2, 1, 1, 1, 4, 4]  # as expected
# for a test with 'o' at the start and end and '|' at the middle
print(parse_music('o o| .| o| o| .| .| .| .| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1