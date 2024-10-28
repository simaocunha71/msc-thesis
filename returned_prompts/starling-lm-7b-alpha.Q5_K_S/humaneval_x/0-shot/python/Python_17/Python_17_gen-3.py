def parse_music(music_string: str) -> List[int]:
    # Initialize an empty list to store the beats
    beats = []
    # Iterate over the string
    for char in music_string:
        # Check if the character is an 'o'
        if char == 'o':
            # If so, add 4 to the list
            beats.append(4)
        # Check if the character is an 'o' followed by a '|'
        elif char == 'o|':
            # If so, add 2 to the list
            beats.append(2)
        # Check if the character is a '.' followed by a '|'
        elif char == '.':
            # If so, add 1 to the list
            beats.append(1)
    return beats

# Test the function
print(parse_music('o o| .| o| o| .| .| .| .| o o'))

# Output:
# [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]


