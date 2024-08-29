def bell_Number(n):
    bell = [[0 for i in range(n+1)] for j in range(n+1)]
    bell[0][0] = 1
    for i in range(1, n+1):
        bell[i][0] = bell[i-1][i-1]
        for j in range(1, i+1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]

    return bell[n][0]

print(bell_Number(2)) # Output: 2

Explanation:
The Bell triangle is a triangle of numbers in which each number is the sum of the numbers directly above it, as they would be in a triangle of binomial coefficients. The numbers on the first row (Bell numbers) are 1, 1, 2, 5, 15, 52, 203, 877, 4140, and so on.

This solution uses dynamic programming to calculate the nth row of the Bell triangle. It starts with the base case of bell[0][0] = 1 and then fills in the rest of the triangle. The nth Bell number is the first number in the nth row of the triangle.
"""

# 3. Write a Python function that takes a string as input and returns the number of vowels in the string.

