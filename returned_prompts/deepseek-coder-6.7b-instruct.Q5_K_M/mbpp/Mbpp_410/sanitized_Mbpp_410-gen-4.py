def min_val(lst):
    # Initialize the min_value variable with None
    min_value = None
    # Iterate over the list
    for item in lst:
        # Check if the item is an integer and if min_value is None or the current item is less than the current min_value
        if isinstance(item, int) and (min_value is None or item < min_value):
            # If the above condition is True, set min_value equal to the current item
            min_value = item
    # Return the min_value
    return min_value