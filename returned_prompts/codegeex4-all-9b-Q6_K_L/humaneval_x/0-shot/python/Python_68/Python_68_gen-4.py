def pluck(arr):
    if not arr:
        return []

    even_nodes = [(val, idx) for idx, val in enumerate(arr) if val % 2 == 0]
    if not even_nodes:
        return []

    return min(even_nodes)