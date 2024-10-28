def Find_Min_Length(input_list):
    """This function takes in a list of lists and returns the length of the smallest list in the list."""
    smallest_length = len(input_list[0])
    for i in range(len(input_list)):
        if len(input_list[i]) < smallest_length:
            smallest_length = len(input_list[i])
    return smallest_length