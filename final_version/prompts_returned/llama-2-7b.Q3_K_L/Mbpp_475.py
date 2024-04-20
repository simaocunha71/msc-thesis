"""
Write a function to sort a dictionary by value.
assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]
"""

def sort(dict):
    sorted_dict = dict.copy() # Make a copy of the dictionary to allow for modification.

    # Add keys in ascending order and values in descending order
    for key, value in sorted(sorted_dict.items(), key=lambda item: item[1], reverse=True):
        sorted_dict[key] = value  # Replace with the ordered version of the value

    return sorted_dict
