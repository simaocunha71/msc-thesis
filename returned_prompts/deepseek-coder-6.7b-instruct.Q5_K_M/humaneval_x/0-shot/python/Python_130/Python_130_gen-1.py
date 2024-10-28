
def tri(n):
    sequence = [1, 3, 2]
    if n < 3:
        return sequence[:n+1]
    for i in range(3, n):
        if i % 2 == 0:
            sequence.append(1 + i // 2)
        else:
            sequence.append(sequence[-1] + sequence[-2] + sequence[-3])
    sequence.append(sequence[-1] + sequence[-2] + sequence[-3])
    return sequence


print(tri(3))
print(tri(4))
print(tri(5))
print(tri(6))
print(tri(7))
print(tri(8))
print(tri(9))
print(tri(10))
print(tri(11))
print(tri(12))
print(tri(13))
print(tri(14))
print(tri(15))
print(tri(16))
print(tri(17))
print(tri(18))
print(tri(19))
print(tri(20))


"""
The output should be:
[1, 3, 2, 8]
[1, 3, 2, 8, 15]
[1, 3, 2, 8, 15, 29]
[1, 3, 2, 8, 15, 29, 56]
[1, 3, 2, 8, 15, 29, 56, 120]
[1, 3, 2, 8, 15, 29, 56, 120, 297]
[1, 3, 2, 8, 15, 29, 56, 120, 297, 812]
[1, 3, 2, 8, 15, 29, 56, 120, 297, 812, 2275]
[1, 3, 2, 8, 15, 2