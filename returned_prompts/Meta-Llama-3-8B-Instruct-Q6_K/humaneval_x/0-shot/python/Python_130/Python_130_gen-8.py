def tri(n):
    if n == 0:
        return []
    elif n == 1:
        return [3]
    elif n == 2:
        return [3, 2]
    else:
        seq = [3, 2]
        for i in range(2, n):
            if i % 2 == 0:
                seq.append(1 + i / 2)
            else:
                seq.append(seq[i-1] + seq[i-2] + seq[i-3])
        return seq

print(tri(3)) # [1, 3, 2, 8]
print(tri(4)) # [1, 3, 2, 8, 3]
print(tri(5)) # [1, 3, 2, 8, 3, 10]  # 3.5 not a integer, so round up to 4
print(tri(6)) # [1, 3, 2, 8, 3, 10, 13]
print(tri(7)) # [1, 3, 2, 8, 3, 10, 13, 18]
print(tri(8)) # [1, 3, 2, 8, 3, 10, 13, 18, 29]
print(tri(9)) # [1, 3, 2, 8, 3, 10, 13, 18, 29, 47]
print(tri(10)) # [1, 3, 2, 8, 3, 10, 13, 18, 29, 47, 76]
print(tri(11)) # [1, 3, 2, 8, 3, 10, 13, 18, 29, 47, 76, 123]
print(tri(12)) # [1, 3, 2, 8, 3, 10, 13, 18, 29, 47, 76, 123, 199]  # 198 not a integer, so round up to 199
print(tri(13)) # [1, 3, 2, 8, 3, 10, 13, 18, 29, 47, 76, 123, 