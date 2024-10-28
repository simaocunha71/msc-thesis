def tri(n):
    if n == 0: return [3]
    if n == 1: return [1, 3]
    res = [1, 3]
    for i in range(2, n):
        if i % 2 == 0:
            res.append(1 + i / 2)
        else:
            res.append(res[i - 1] + res[i - 2] + res[i + 1])
    return res

print(tri(3))