    l = sorted(l)
    return [l[i] if i % 3 != 0 else l[i - 1] for i in range(len(l))]
