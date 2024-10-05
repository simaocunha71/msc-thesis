    if not arr:
        return []
    smallest_even_value = float('inf')
    smallest_even_index = -1
    for i, value in enumerate(arr):
        if value % 2 == 0 and value < smallest_even_value:
            smallest_even_value = value
            smallest_even_index = i
    if smallest_even_value == float('inf'):
        return []
    return [smallest_even_value, smallest_even_index]  # Return the smallest even value and its index


