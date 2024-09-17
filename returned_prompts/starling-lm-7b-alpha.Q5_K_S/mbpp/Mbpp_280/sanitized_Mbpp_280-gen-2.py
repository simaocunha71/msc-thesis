def sequential_search(array, element):
    # Iterate through the array
    for i in range(len(array)):
        # Check if the element is found
        if array[i] == element:
            # Return a tuple with the boolean and the index
            return (True, i)
    # Return a tuple with the boolean and the index if not found
    return (False, -1)