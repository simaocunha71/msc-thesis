def tri(n):
    if n == 0: return [1]
    if n == 1: return [1, 3]
    if n == 2: return [1, 3, 2]
    if n == 3: return [1, 3, 2, 8]
    tri_seq = [1, 3, 2, 8]
    for i in range(n-3):
        if i % 2 == 0:
            tri_seq.append(1 + i / 2)
        else:
            tri_seq.append(tri_seq[i-1] + tri_seq[i-2] + tri_seq[i+1])
    return tri_seq

print(tri(3))