    third_indices = [i for i in range(len(l)) if i % 3 == 0]
    third_values = sorted([l[i] for i in third_indices])
    for idx, val in zip(third_indices, third_values):
        l[idx] = val
    return l

