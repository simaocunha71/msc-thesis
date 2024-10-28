

def triples_sum_to_zero(l: list) -> bool:
    """
    This function takes a list of integers as an input.
    It returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """

    # Initialize the counter to 0
    counter = 0

    # Create a dictionary to store the elements in the list
    elements_dict = {}

    # Iterate through the list of integers
    for elem in l:
        # If the element is already in the dictionary, increment its value by 1
        if elem in elements_dict:
            elements_dict[elem] += 1
        # If the element is not in the dictionary, add it with a value of 1
        else:
            elements_dict[elem] = 1

    # Iterate through the dictionary of elements
    for key1 in elements_dict:
        # If the element is negative, increment the counter by the absolute value of the element
        if key1 < 0:
            counter += -1 * abs(key1)
        # Iterate through the dictionary again
        for key2 in elements_dict:
            # If the element is negative, increment the counter by the absolute value of the element
            if key2 < 0:
                counter += -1 * abs(key2)
            # If the element is not the same as the previous element, add the absolute value of the elements
            elif key1 != key2:
                counter += abs(key1) + abs(key2)
            # If the element is the same as the previous element, increment the counter by the absolute value of the element
            else:
                counter += 2 * abs(key1)
            # If the counter is equal to 0, return True
            if counter == 0:
                return True
    # If the counter is not equal to 0, return False
    return False


# Test cases
print(triples_sum_to_zero([1, 3, 5, 0]))  # False
print(triples_sum_to_zero([1, 3, -2, 1]))  # True
print(triples_