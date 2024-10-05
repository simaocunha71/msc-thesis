    even_indices = [l[i] for i in range(0, len(l), 2)]
    sorted_even_indices = sorted(even_indices)

    for i in range(0, len(l), 2):
        l[i] = sorted_even_indices[i // 2]

    return l

