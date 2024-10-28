    if not arr:
        return []

    even_values = [(value, index) for index, value in enumerate(arr) if value % 2 == 0]

    if not even_values:
        return []

    smallest_value, smallest_index = min(even_values)

    return [smallest_value, smallest_index]

