def first_non_repeating_character(str):
    '''
    This function will return the first non-repeated character in the string
    '''
    # Create a dictionary to count the occurrence of each character
    char_count = {}
    for char in str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Traverse the string and find the first non-repeated character
    for char in str:
        if char_count[char] == 1:
            return char

    # Return None if no non-repeated character is found
    return None