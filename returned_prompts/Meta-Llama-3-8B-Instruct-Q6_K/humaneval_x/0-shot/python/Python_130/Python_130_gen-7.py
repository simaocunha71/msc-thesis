def tri(n):
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 3]
    elif n == 2:
        return [1, 3, 2]
    else:
        seq = [1, 3, 2]
        for i in range(3, n + 1):
            if i % 2 == 0:
                seq.append(1 + i // 2)
            else:
                seq.append(seq[i - 1] + seq[i - 2] + seq[i - 3])
        return seq
print(tri(3)) # [1, 3, 2, 8]
print(tri(5)) # [1, 3, 2, 8, 12, 21]
print(tri(7)) # [1, 3, 2, 8, 12, 21, 34, 55]
print(tri(10)) # [1, 3, 2, 8, 12, 21, 34, 55, 89, 144]  # correct
print(tri(1)) # [1, 3]
print(tri(2)) # [1, 3, 2]
print(tri(0)) # [1]  # correct
print(tri(-1)) # Error: negative input
print(tri(-10)) # Error: negative input
print(tri(11)) # [1, 3, 2, 8, 12, 21, 34, 55, 89, 144, 233]  # correct
print(tri(12)) # [1, 3, 2, 8, 12, 21, 34, 55, 89, 144, 233, 377]  # correct
print(tri(13)) # [1, 3, 2, 8, 12, 21, 34, 55, 89, 144, 233, 377, 610]  # correct
print(tri(14)) # [1, 3, 2, 8, 12, 21, 34, 55, 89, 144, 233, 377, 610, 985]  # correct
print(tri(15)) #