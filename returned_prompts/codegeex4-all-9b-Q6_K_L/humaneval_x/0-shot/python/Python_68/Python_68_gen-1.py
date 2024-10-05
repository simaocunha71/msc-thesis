def pluck(arr):
    # Initialize the smallest even value and its index to None
    smallest_even_value = None
    smallest_even_index = None
    
    # Iterate over the array
    for index, value in enumerate(arr):
        # Check if the value is even
        if value % 2 == 0:
            # If it's the first even value we found, or it's smaller than the current smallest even value,
            # update the smallest even value and its index
            if smallest_even_value is None or value < smallest_even_value:
                smallest_even_value = value
                smallest_even_index = index
    
    # If we found an even value, return it and its index, otherwise return an empty list
    if smallest_even_value is not None:
        return [smallest_even_value, smallest_even_index]
    else:
        return []

# Test the function with the provided examples
print(pluck([4,2,3])) # [2, 1]
print(pluck([1,2,3])) # [2, 1]
print(pluck([])) # []
print(pluck([5, 0, 3, 0, 4, 2])) # [0, 1]