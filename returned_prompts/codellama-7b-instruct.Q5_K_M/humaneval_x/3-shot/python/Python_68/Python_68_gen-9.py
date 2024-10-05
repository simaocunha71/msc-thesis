    even_nodes = [node for node in arr if node % 2 == 0]
    if not even_nodes:
        return []

    sorted_even_nodes = sorted(even_nodes)
    smallest_even_value = sorted_even_nodes[0]
    smallest_even_value_index = even_nodes.index(smallest_even_value)

    return [smallest_even_value, smallest_even_value_index]


