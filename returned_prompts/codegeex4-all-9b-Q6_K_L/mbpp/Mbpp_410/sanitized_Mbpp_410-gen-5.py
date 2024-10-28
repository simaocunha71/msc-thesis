def min_val(lst):
    # Filter the list to only include numbers
    numbers = [x for x in lst if isinstance(x, (int, float))]
    # Return the minimum value or None if no numbers are found
    return min(numbers) if numbers else None