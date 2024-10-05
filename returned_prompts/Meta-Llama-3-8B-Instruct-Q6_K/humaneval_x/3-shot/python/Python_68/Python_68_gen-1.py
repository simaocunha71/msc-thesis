    even_nodes = [node for node in arr if node % 2 == 0]
    if not even_nodes:
        return []
    smallest_even = min(even_nodes)
    return [smallest_even, arr.index(smallest_even)]


