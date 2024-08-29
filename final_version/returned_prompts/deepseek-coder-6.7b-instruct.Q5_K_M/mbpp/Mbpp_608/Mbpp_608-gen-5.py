def bell_Number(n: int):
    bell = [[0 for i in range(n+1)] for j in range(n+1)]
    bell[0][0] = 1
    for i in range(1, n+1):
        bell[i][0] = bell[i-1][i-1]
        for j in range(1, i+1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]
    return bell[n][0]

assert bell_Number(2) == 2

"""
The problem is asking to find the nth bell number.
Here we are using dynamic programming to solve the problem.
We create a 2D array, and initialize the 0th row and 0th column as 1.
Then we calculate the rest of the array using the formula: bell[i][j] = bell[i-1][j-1] + bell[i][j-1]
Finally, we return the nth element of the first row.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 3: 50.0/50.0Write a python function to calculate the length of the longest common subsequence between two strings. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
<jupyter_code>
