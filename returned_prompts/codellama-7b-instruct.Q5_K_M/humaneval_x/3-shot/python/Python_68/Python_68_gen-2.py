    even_nodes = []
    for idx, node in enumerate(arr):
        if node % 2 == 0:
            even_nodes.append((node, idx))

    return [node for node in even_nodes if node[0] == min(even_nodes, key=lambda x: x[0])][0]


