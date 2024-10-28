def first_non_repeating_character(s):
    # initialize a dictionary to store the frequency of characters
    char_count = {}

    # count the frequency of each character in the string
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_tuple = (char, 1)
            char_count[char] = 1

    # iterate through the string and return the first character that has a count of 1
    for char in s:
        if char_count[char] == 1:
            return char

    # return None if no characters are non-repeating
    return None