    if n == 0:
        return [3]

    if n == 1:
        return [3]

    if n == 2:
        return [3, 2]

    tri_seq = [3, 2]
    for i in range(3, n + 1):
        if i % 2 == 0:
            tri_seq.append(1 + i / 2)
        else:
            tri_seq.append(tri_seq[i - 1] + tri_seq[i - 2] + tri_seq[i - 3])

    return tri_seq


