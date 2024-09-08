def count_char_position(s):
    # Initialize counter
    counter = 0
    # Iterate over the string
    for i in range(len(s)):
        # Compare the character with its position in the English alphabet (case insensitive)
        if s[i].lower() == chr(97+i).lower():
            # Increase the counter
            counter += 1
    # Return the counter
    return counter