def get_ludic(n):
    ludic = [1]
    for i in range(1, n):
        j = 0
        while i + j < n:
            j = ludic[j] + 1
        ludic.append(j)
    return ludic