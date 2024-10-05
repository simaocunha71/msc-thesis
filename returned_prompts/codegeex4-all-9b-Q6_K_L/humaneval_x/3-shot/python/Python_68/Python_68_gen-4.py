    even_nodes = sorted([node for node in arr if node % 2 == 0])
    if even_nodes:
        return [even_nodes[0], arr.index(even_nodes[0])]
    else:
        return []

