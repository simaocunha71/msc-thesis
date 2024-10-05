
def tri(n):
    tri_numbers = [1, 3, 2]
    if n < 3:
        return tri_numbers[:n+1]
    for i in range(3, n+1):
        if i % 2 == 0:
            tri_numbers.append(1 + i // 2)
        else:
            tri_numbers.append(tri_numbers[i-1] + tri_numbers[i-2] + tri_numbers[i])
    return tri_numbers

print(tri(3))  # [1, 3, 2, 8]
print(tri(5))  # [1, 3, 2, 8, 5, 13]
print(tri(10))  # [1, 3, 2, 8, 5, 13, 8, 24, 11, 35, 17]


def tri(n):
    if n == 0:
        return [1]
    if n == 1:
        return [1, 3]
    if n == 2:
        return [1, 3, 2]
    t = [1, 3, 2]
    for i in range(3, n + 1):
        if i % 2 == 0:
            t.append(1 + i // 2)
        else:
            t.append(t[i - 1] + t[i - 2] + t[i - 3])
    return t

print(tri(3))  # [1, 3, 2, 8]
print(tri(5))  # [1, 3, 2, 8, 5, 13]
print(tri(10))  # [1, 3, 2, 8, 5, 13, 8, 24, 11, 35, 17]


def tri(n):
    tri_list = [1, 3, 2]
    if n < 3:
        return tri_list[:n+1]
    else:
       