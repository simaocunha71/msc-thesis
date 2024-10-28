    if n == 0:
        return [1]
    elif n == 1:
        return [1, 3]
    elif n == 2:
        return [1, 3, 2]

    tri_seq = [1, 3, 2]
    for i in range(3, n+1):
        if i % 2 == 0:
            tri_seq.append(2)
        else:
            tri_seq.append(tri_seq[-1] + tri_seq[-2] + tri_seq[-3])

    return tri_seq


