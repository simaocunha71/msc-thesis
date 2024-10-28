    even_nodes = [(index, value) for index, value in enumerate(arr) if value % 2 == 0]
    return [even_nodes[0][1], even_nodes[0][0]] if even_nodes else []


