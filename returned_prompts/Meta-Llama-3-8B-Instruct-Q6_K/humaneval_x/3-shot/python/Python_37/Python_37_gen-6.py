    return [i if i % 2 != 0 else sorted([j for j in l if j % 2 == 0])[-1] for i in l]  # O(n log n)


