    even_indicies = [i for i in range(len(l)) if i % 2 == 0]
    sorted_values = sorted([l[i] for i in even_indicies])
    for i, value in zip(even_indicies, sorted_values):
        l[i] = value
    return l


