    l = list(l)
    third_indices = [i for i in range(len(l)) if i % 3 == 0]
    third_values = [l[i] for i in third_indices]
    third_values.sort()
    for i, v in zip(third_indices, third_values):
        l[i] = v
    return l

