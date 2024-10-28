    even_nodes = []
    for idx, node in enumerate(arr):
        if node % 2 == 0:
            even_nodes.append((node, idx))

    if not even_nodes:
        return []

    smallest_even_value, smallest_even_index = min(even_nodes, key=lambda t: t[0])

    return [smallest_even_value, smallest_even_index]


