    evens = [node for i, node in enumerate(arr) if node % 2 == 0]
    if not evens:
        return []
    return [min(evens, key=lambda x: (x % 2, i)) if evens else []]


