
def bell_number(n):
    bell = [[0 for i in range(n+1)] for j in range(n+1)]
    bell[0][0] = 1
    for i in range(1, n+1):
        bell[i][0] = bell[i-1][i-1]
        for j in range(1, i+1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]
    return bell[n][0]

print(bell_number(2))  # 2

Explanation:

A Bell number is a sequence of numbers that appears in various counting problems in combinatorics. The sequence of Bell numbers starts 1, 1, 2, 5, 15, 52, 203, 877, 4140, 21147, ...

