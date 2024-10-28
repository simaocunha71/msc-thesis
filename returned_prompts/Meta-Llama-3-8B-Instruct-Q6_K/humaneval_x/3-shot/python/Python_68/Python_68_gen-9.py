    if not arr:
        return []

    even_nodes = [node for node in arr if node % 2 == 0]
    if not even_nodes:
        return []

    smallest_value = min(even_nodes)
    smallest_index = arr.index(smallest_value)

    return [smallest_value, smallest_index]  # Return as a list


