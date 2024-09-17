
def sequence(n):
    if n < 1:
        return []
    if n == 1:
        return [1]
    res = [1, 1]
    for i in range(2, n):
        res.append(res[res[i-1]-1] + res[i-res[i-1]])
    return res[-1]


