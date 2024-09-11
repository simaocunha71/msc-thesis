"""
def Extract(input_list):
    # Create an empty list
    output_list = []

    # Iterate through the input_list
    for sublist in input_list:
        # Append the first element of the sublist to the output_list
        output_list.append(sublist[0])
    return output_list

print(Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]))
"""

# This will output: [1, 3, 6]

def Extract(input_list):
    # Create an empty list
    output_list = []

    # Iterate through the input_list
    for sublist in input_list:
        # Append the first element of the sublist to the output_list
        output_list.append(sublist[0])
    return output_list

# Test the function
print(Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]))
# This will output: [1, 3, 6]


# Another approach
def Extract(input_list):
    # Flatten the list
    flat_list = [item for sublist in input_list for item in sublist]
    # Return the first item of the flattened list
    return flat_list[0]

# Test the function
print(Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]))
# This will output: 1


# Yet another approach
def Extract(input_list):
    # Convert the list to a generator object
    generator = (sublist[0] for sublist in input_list)
    # Return the first item of the generator object
    return next(generator)

# Test the function
print(Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]))
# This will output: 1


# The most Pythonic approach
def Extract(input_list):
    # Use a list comprehens