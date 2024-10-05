    even_nodes = []
    for idx, elem in enumerate(arr):
        if elem % 2 == 0:
            even_nodes.append([elem, idx])

    if len(even_nodes) == 0:
        return []

    return min(even_nodes)


