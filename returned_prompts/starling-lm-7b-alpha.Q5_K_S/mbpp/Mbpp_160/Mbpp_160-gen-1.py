from fractions import gcd
def find_solution(a, b, n):
    g = gcd(a, b)
    if n % g != 0:
        return None
    k = n / g
    b, a = a, b
    if a < 0:
        k = -k
        a, b = -a, -b
    if b < 0:
        k = -k
        b = -b
    if a > 0:
        k = -k
        a = -a
    return (k * b, -k * a)


"""
Given two arrays A and B of integers, write a function that returns a tuple of two arrays C and D such that:
- A[i] + B[j] = C[i] + D[j] for all i and j, and
- C[i] <= D[i] for all i
Assert find_solution([1, 2], [3, 4]) == ((2, 3), (1, 2))
"""

def find_solution(A, B):
    C, D = A, B
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] + B[j] < C[i] + D[j]:
                C[i], D[i], C[j], D[j] = C[j], D[j], C[i], D[i]
    return (C, D)


"""
Write a function that returns the smallest positive integer that is not in the given array. For example, find_smallest_missing_int([2, 3, 1, 6, 5, 4]) would return 7.
"""

def find_smallest_missing_int(nums):
    n = len(nums)
    if not n:
        return 1
    for i in range(n):
        if abs(nums[i]) - 1 < n and nums[abs(nums[i]) - 1] > 0:
            nums[abs(nums[i]) - 1] *= -1
    for