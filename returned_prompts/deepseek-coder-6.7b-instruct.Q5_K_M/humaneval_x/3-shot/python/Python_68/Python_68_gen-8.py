    smallest_even_value = None
    smallest_even_index = None

    for index, value in enumerate(arr):
        if value % 2 == 0:
            if smallest_even_value is None or value < smallest_even_value:
                smallest_even_value = value
                smallest_even_index = index

    if smallest_even_value is not None:
        return [smallest_even_value, smallest_even_index]
    else:
        return []


