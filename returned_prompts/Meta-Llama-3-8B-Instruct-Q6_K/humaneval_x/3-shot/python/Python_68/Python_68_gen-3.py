    if not arr:
        return []

    even_nodes = [(x, i) for i, x in enumerate(arr) if x % 2 == 0]
    if not even_nodes:
        return []

    min_even_node = min(even_nodes, key=lambda x: (x[0], x[1]))
    return [min_even_node[0], min_even_node[1]]


