"""
def odd_values_string(input_string):
    # Convert the string to a list
    input_list = list(input_string)
    # Create an empty list to store the characters with even index values
    output_list = []
    # Loop through the list
    for index, char in enumerate(input_list):
        # Check if index is even
        if index % 2 == 0:
            # Append the character to the output list
            output_list.append(char)
    # Convert the output list back to a string
    output_string = "".join(output_list)
    # Return the output string
    return output_string

# Test the function
odd_values_string('abcdef')  # Returns 'ace'
"""

def odd_values_string(input_string):
    # Convert the string to a list
    input_list = list(input_string)
    # Create an empty list to store the characters with even index values
    output_list = []
    # Loop through the list
    for index, char in enumerate(input_list):
        # Check if index is even
        if index % 2 == 0:
            # Append the character to the output list
            output_list.append(char)
    # Convert the output list back to a string
    output_string = "".join(output_list)
    # Return the output string
    return output_string

# Test the function
odd_values_string('abcdef')  # Returns 'ace'








def odd_values_string(input_string):
    # Convert the string to a list
    input_list = list(input_string)
    # Create an empty list to store the characters with even index values
    output_list = []
    # Loop through the list
    for index, char in enumerate(input_list):
        # Check if index is even
        if index % 2 == 0:
            # Append the character to the output list
            output_list.append(char)
    # Convert the output list back to a string
    output_string = "".join(output_list)
    # Return the output string