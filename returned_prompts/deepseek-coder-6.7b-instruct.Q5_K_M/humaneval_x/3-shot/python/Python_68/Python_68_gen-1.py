    even_nodes = [(v, i) for i, v in enumerate(arr) if v % 2 == 0]
    return min(even_nodes, default=([], ))[0] if even_nodes else []

