def tri(n):
    if n == 0:
        return [1]
    if n == 1:
        return [1, 3]
    seq = [1, 3]
    for i in range(n-1):
        if i % 2 == 0:
            seq.append(1 + i/2)
        else:
            seq.append(seq[-1] + seq[-2] + seq[-3])
    return seq

# Test cases
print(tri(0))  # [1]
print(tri(1))  # [1, 3]
print(tri(2))  # [1, 3, 2]
print(tri(3))  # [1, 3, 2, 8]
print(tri(4))  # [1, 3, 2, 8, 5]
print(tri(5))  # [1, 3, 2, 8, 5, 14]