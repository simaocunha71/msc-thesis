    even_values = []
    smallest_even_value = float("inf")
    smallest_index = -1

    for i, node in enumerate(arr):
        if node % 2 == 0:
            even_values.append(node)
            if node < smallest_even_value:
                smallest_even_value = node
                smallest_index = i

    if not even_values:
        return []

    return [smallest_even_value, smallest_index]
