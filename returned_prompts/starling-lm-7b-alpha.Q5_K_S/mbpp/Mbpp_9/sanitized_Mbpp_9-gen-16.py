def find_Rotations(word):
    # Convert the string to a list
    word_list = list(word)
    # Create an empty dictionary
    result = {}
    # Iterate through the list and add the first letter as a key in the dictionary
    for i in range(len(word_list)):
        result[word_list[i]] = i
    # Rotate the list by one to compare with the original dictionary
    rotated_list = word_list[1:] + word_list[:1]
    # Initialize the minimum number of rotations to 0
    min_rotations = 0
    # Iterate through the rotated list to find the index of the first letter
    for i in range(len(rotated_list)):
        if rotated_list[i] in result:
            # If the index of the first letter in the rotated list is less than the original index, increment min_rotations
            if result[rotated_list[i]] < i:
                min_rotations += 1
            # If the index of the first letter in the rotated list is greater than the original index, break the loop
            else:
                break
    # Return the minimum number of rotations
    return min_rotations