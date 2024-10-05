def parse_music(music_string: str) -> List[int]:
    # Initialize an empty list to store the lengths of the notes.
    lengths = []
    # Iterate through the string.
    for note in music_string:
        # If the note is a whole note, append 4 to the list.
        if note == 'o':
            lengths.append(4)
        # If the note is a half note, append 2 to the list.
        elif note == 'o|':
            lengths.append(2)
        # If the note is a quarter note, append 1 to the list.
        elif note == '.|':
            lengths.append(1)

    # Return the list of note lengths.
    return lengths

# Here are some test cases to check if your code is correct.
print(parse_music('o o| .| o| o| o'))  # Returns [4, 2, 1, 2, 2]
print(parse_music('o o| .| o| o| .| .| .| .| o o'))  # Returns [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]



# Here's a step-by-step guide to solving this problem.

# Step 1: Identify the different types of notes and their corresponding values.
# Here is a legend for the notes:
# 'o' - whole note, lasts four beats
# 'o|' - half note, lasts two beats
# '.|' - quater note, lasts one beat

# Step 2: Initialize an empty list to store the lengths of the notes.
# lengths = []

# Step 3: Iterate through the music string.
# For each note, check if it is a whole note, half note, or quarter note and append the appropriate value to the list.

# Step 4: Return the list of note lengths.
# Here's a visual guide to understanding how the music string is parsed:
# Input: 'o o| .| o| o| o'
# Output: [4, 2, 1, 2