"""
Firstly, the function will take an integer n as input. The function will calculate the nth bell number by following the formula:

bell(n) = sum(bell(i)*bell(n-i-1) for i in range(n+1))

where,

bell(0) = 1
bell(1) = 1

The function will use these recursive calls to calculate the nth bell number.

"""

def bell_number(n):
    bell = [[0 for i in range(n+1)] for j in range(n+1)]
    bell[0][0] = 1
    for i in range(1, n+1):
        # Explicitly fill for j = 0
        bell[i][0] = bell[i-1][i-1]
        # Fill for remaining values of j
        for j in range(1, i+1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]
    return bell[n][0]


print(bell_number(2))

# Test Cases
assert bell_number(2) == 2
assert bell_number(3) == 5
assert bell_number(4) == 15
assert bell_number(5) == 52
assert bell_number(6) == 203
assert bell_number(7) == 877
assert bell_number(8) == 4140
assert bell_number(9) == 21147
assert bell_number(10) == 115975

# 