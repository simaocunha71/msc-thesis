def odd_Equivalent(binary_string, number_of_rotations):
    # Initialize a list to store the binary string
    binary_list = list(binary_string)

    # Rotate the list the given number of times
    for i in range(number_of_rotations):
        binary_list.append(binary_list.pop(0))

    # Initialize a count to store the number of odd values
    count = 0

    # Iterate over the list
    for binary_value in binary_list:
        # Check if the binary value is odd
        if binary_value == "1":
            # Increment the count
            count += 1

    # Return the count
    return count