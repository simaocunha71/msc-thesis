    even_indices = [l[i] for i in range(len(l)) if i % 2 == 0]
    even_indices.sort()
    for i in range(len(l)):
        if i % 2 == 0:
            l[i] = even_indices.pop(0)