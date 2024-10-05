    indices = [i for i in range(len(l)) if (i + 1) % 3 == 0]
    values = sorted([l[i] for i in indices])
    for i, v in zip(indices, values):
        l[i] = v
    return l


