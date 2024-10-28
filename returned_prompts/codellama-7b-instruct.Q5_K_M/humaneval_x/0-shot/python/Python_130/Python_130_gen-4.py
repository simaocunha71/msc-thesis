
def tri(n):
    tri = [1, 3]
    for i in range(2, n+1):
        if i % 2 == 0:
            tri.append(1 + i/2)
        else:
            tri.append(tri[i-1] + tri[i-2] + tri[i+1])
    return tri