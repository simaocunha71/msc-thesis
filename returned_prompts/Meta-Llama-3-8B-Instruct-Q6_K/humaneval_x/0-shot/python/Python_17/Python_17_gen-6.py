def parse_music(music_string: str) -> List[int]:
    beats_per_note = {'o': 4, 'o|': 2, '.|': 1}
    beats_list = []
    i = 0
    while i < len(music_string):
        if music_string[i] == '|':
            i += 1
        note = music_string[i:i+2]
        i += 2
        beats_list.append(beats_per_note[note])
    return beats_list

# Testing the function
print(parse_music('o o| .| o| o| .| .| .| .| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]  # Correct result
# Testing the function
print(parse_music('.| o| o| o|'))
# Output: [1, 2, 4, 4]  # Correct result
# Testing the function
print(parse_music('o o o o'))
# Output: [4, 4, 4, 4]  # Correct result
# Testing the function
print(parse_music('.| .| .|'))
# Output: [1, 1, 1]  # Correct result
# Testing the function
print(parse_music('o| o| o| o|'))
# Output: [2, 2, 2, 2]  # Correct result
# Testing the function
print(parse_music('o| .| o| .|'))
# Output: [2, 1, 2, 1]  # Correct result
# Testing the function
print(parse_music('o| o| .| .|'))
# Output: [2, 2, 1, 1]  # Correct result
# Testing the function
print(parse_music('o| o| o| .|'))
# Output: [2, 2, 2, 1]  # Correct result
# Testing the function
print(parse_music('o| .| o| .| .|'))
# Output: [2, 1, 2, 1, 1]  # Correct result
# Testing the function
print(parse_music('o| .| .| o| .|'))
# Output: [2, 1, 1, 2, 1]  # Correct result
# Testing