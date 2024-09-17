def Extract(input_list):
    # Create an empty list
    output_list = []

    # Iterate through the input_list
    for sublist in input_list:
        # Append the first element of the sublist to the output_list
        output_list.append(sublist[0])
    return output_list