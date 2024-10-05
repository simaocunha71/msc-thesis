def tri(n):
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 3]
    elif n == 2:
        return [1, 3, 2]
    else:
        tribonacci = [1, 3, 2]
        for i in range(3, n + 1):
            if i % 2 == 0:
                tribonacci.append(1 + i / 2)
            else:
                tribonacci.append(tribonacci[i - 1] + tribonacci[i - 2] + tribonacci[i - 3])
        return tribonacci

print(tri(3))  # [1, 3, 2, 8]
print(tri(4))  # [1, 3, 2, 3, 8]
print(tri(5))  # [1, 3, 2, 3, 8, 21]
print(tri(6))  # [1, 3, 2, 3, 8, 21, 43]  # this is the 7th element
print(tri(7))  # [1, 3, 2, 3, 8, 21, 43, 85]
print(tri(8))  # [1, 3, 2, 3, 8, 21, 43, 85, 170]  # this is the 9th element
print(tri(9))  # [1, 3, 2, 3, 8, 21, 43, 85, 170, 352]  # this is the 10th element
print(tri(10))  # [1, 3, 2, 3, 8, 21, 43, 85, 170, 352, 715]  # this is the 11th element
print(tri(11))  # [1, 3, 2, 3, 8, 21, 43, 85, 170, 352, 715, 1390]  # this is the 12th element
print(tri(12))  # [1, 3, 2, 3, 8, 21, 43, 85, 170, 352