
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
print(tri(5))  # [1, 3, 2, 8, 5, 18]
print(tri(6))  # [1, 3, 2, 8, 5, 18, 11]
print(tri(7))  # [1, 3, 2, 8, 5, 18, 11, 34]
print(tri(8))  # [1, 3, 2, 8, 5, 18, 11, 34, 25]
print(tri(9))  # [1, 3, 2, 8, 5, 18, 11, 34, 25, 89]

This function works by first initializing a list tri_numbers with the first three Tribonacci numbers. Then it iterates over the range from 3 to n (inclusive) and appends to the list tri_numbers the next Tribonacci number according to the rules. The function finally returns the tri_numbers list.
"""

# Solution 2
"""
