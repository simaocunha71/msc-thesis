
def tri(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 3]
    else:
        res = [1, 3, 2]
        for i in range(3, n+1):
            if i % 2 == 0:
                res.append(1 + i / 2)
            else:
                res.append(res[i-1] + res[i-2] + res[i-3])
        return res

# print(tri(3)) # [1, 3, 2, 8]
# print(tri(4)) # [1, 3, 2, 8, 1]






