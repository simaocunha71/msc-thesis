    if n == 0:
        return [3]
    elif n == 1:
        return [3]
    elif n == 2:
        return [3, 2]
    else:
        tri_sequence = [3, 2]
        for i in range(2, n):
            if i % 2 == 0:
                tri_sequence.append(1 + i / 2)
            else:
                tri_sequence.append(tri_sequence[i - 1] + tri_sequence[i - 2] + tri_sequence[i - 3])
        return tri_sequence
