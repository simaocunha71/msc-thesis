def first_non_repeating_character(s):
    # Create a dictionary to store the count of each character
    char_count = {}
    for c in s:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1

    # Iterate through the string again and return the first character
    # with a count of 1
    for c in s:
        if char_count[c] == 1:
            return c

    # If no non-repeating character is found, return None
    return None