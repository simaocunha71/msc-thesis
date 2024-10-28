    tri_seq = [1, 3, 2]
    for i in range(3, n):
        if tri_seq[i - 1] == 0:
            tri_seq[i - 1] = tri_seq[i - 2] + tri_seq[i - 3] + 1
        else:
            tri_seq.append(tri_seq[i - 1] + tri_seq[i - 2] + tri_seq[i])

    return tri_seq


