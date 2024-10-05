    even_indices_values = sorted([l[i] for i in range(0, len(l), 2)])
    j = 0
    for i in range(0, len(l), 2):
        l[i] = even_indices_values[j]
        j += 1
    return l


