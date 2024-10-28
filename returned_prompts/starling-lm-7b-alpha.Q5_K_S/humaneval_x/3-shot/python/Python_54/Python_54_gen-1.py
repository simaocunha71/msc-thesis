    # Create a dictionary of all the characters in the first string and their corresponding counts
    char_dict = {}
    for c in s0:
        char_dict[c] = char_dict.get(c, 0) + 1

    # Iterate through each character in the second string. If a character is in the dictionary, remove it.
    for c in s1:
        if c in char_dict:
            char_dict[c] -= 1
            if char_dict[c] == 0:
                del char_dict[c]

    # If there are any remaining characters in the dictionary, the two words do not have the same characters.
    return not bool(char_dict)


