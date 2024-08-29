def bell_Number(n):
    # Table to store results of subproblems
    bell = [[0 for i in range(n+1)] for j in range(n+1)]
    bell[0][0] = 1
    for i in range(1, n+1):
        # Explicitly fill for j = 0
        bell[i][0] = bell[i-1][i-1]
        # Fill for remaining values of j
        for j in range(1, i+1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]
    return bell[n][0]

print(bell_Number(2))

"""
Explanation:

The Bell Triangle is a triangle of numbers obtained by the sum of Stirling numbers of the second kind. The first few rows of this triangle are as follows:
1
1   2
2   3   5
5   7  10  15
15 20  27  37  52

The Bell Numbers are the numbers in the second row of this triangle, which are 1, 2, 5, 15, 52, 277, 1760, 13305, 109918, 1036176, 11305320, 138859048, 1906028480, 28002682800, 435911492600 etc.

The function 'bell_Number' finds the nth Bell number by filling up a table 'bell' with the Bell numbers. The 'bell' table is a 2D array where the entry at index [i][j] is the Bell number for i objects and j partitions.
"""

# Test
assert bell_Number(2) == 2
<jupyter_output>
2
<jupyter_text>
Question 2:Write a Python function to find the nth Catalan number. Catalan numbers are a sequence of positive integers that appear in many counting problems in combinatorics.