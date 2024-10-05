    l = sorted(l[::2])
    return [l[i] if i % 2 else l[i - 1] for i in range(len(l))]


