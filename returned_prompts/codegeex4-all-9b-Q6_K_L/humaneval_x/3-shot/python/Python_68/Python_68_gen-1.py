    if not arr:
        return []

    smallest_even = float('inf')
    smallest_even_index = -1

    for index, value in enumerate(arr):
        if value % 2 == 0 and value < smallest_even:
            smallest_even = value
            smallest_even_index = index

    return [smallest_even, smallest_even_index] if smallest_even_index != -1 else []

