def Split(input_list):
    """
    This function takes a list of integers and only returns the odd ones.

    Parameters:
    input_list (list): The list of integers.

    Returns:
    list: The list containing only odd integers.
    """
    # Initialize a result list.
    result = []
    # Iterate over the input list.
    for x in input_list:
        # If the number is odd, add it to the result list.
        if x % 2 != 0:
            result.append(x)
    # Return the result.
    return result