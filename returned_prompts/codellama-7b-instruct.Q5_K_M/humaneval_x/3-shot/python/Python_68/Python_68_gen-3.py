    even_nodes = []
    for index, node in enumerate(arr):
        if node % 2 == 0:
            even_nodes.append((node, index))

    if not even_nodes:
        return []

    return min(even_nodes, key=lambda x: x[0])


