def pluck(arr):
    if not arr: return []

    even_nodes = [(node, idx) for idx, node in enumerate(arr) if node % 2 == 0]
    if not even_nodes: return []

    min_val = min(even_nodes, key=lambda x: x[0])[0]
    return [min_val, arr.index(min_val)]

print(pluck([4,2,3]))
print(pluck([1,2,3]))
print(pluck([]))
print(pluck([5, 0, 3, 0, 4, 2]))