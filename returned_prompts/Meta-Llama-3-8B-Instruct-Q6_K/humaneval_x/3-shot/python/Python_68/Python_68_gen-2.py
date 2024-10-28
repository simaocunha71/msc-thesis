    if not arr:
        return []

    even_nodes = [(node, idx) for idx, node in enumerate(arr) if node % 2 == 0]
    if not even_nodes:
        return []

    smallest_value = min(node for node, _ in even_nodes)
    smallest_node = next((node for node, idx in even_nodes if node == smallest_value), None)
    return [smallest_node, arr.index(smallest_node)]


