def highest_Power_of_2(n):
    p = 0
    while (1 << p) <= n:
        p += 1
    return 1 << (p-1)

print(highest_Power_of_2(10))  # Output: 8

Explanation:
In this function, we start with p = 0 and keep increasing it by 1. In each step, we calculate 2 to the power of p using the left shift operator (1 << p). If the result is less than or equal to n, we continue. Otherwise, we return 2 to the power of (p-1), which is the highest power of 2 that is less than or equal to n.
"""

