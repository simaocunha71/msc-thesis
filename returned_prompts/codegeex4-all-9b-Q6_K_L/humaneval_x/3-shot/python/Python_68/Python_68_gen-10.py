    even_values = [i for i in arr if i % 2 == 0]
    if not even_values:
        return []

    min_value = min(even_values)
    min_index = arr.index(min_value)
    return [min_value, min_index]

