def get_total_number_of_sequences(m, n):
    # Initialize the table
    table = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        table[i][1] = 1
    for j in range(2, n+1):
        for i in range(1, m+1):
            for k in range(i*2, m+1):
                table[k][j] += table[i][j-1]
    return sum([table[i][n] for i in range(1, m+1)])

# Test the function
print(get_total_number_of_sequences(10, 4)) # Output: 4

"""
Explanation:

The function uses dynamic programming to solve the problem. The table table[i][j] represents the number of sequences of length j that end with i. For each j, we iterate through all the possible values of i, and for each i, we iterate through all the possible values of k that k is greater than twice i but less than or equal to m. For each k, we add the number of sequences of length j-1 that end with i to the number of sequences of length j that end with k. Finally, we sum up the numbers in the last column of the table to get the total number of sequences of length n.
"""
<jupyter_output>
4
<jupyter_text>
Question 3:
<jupyter_code>
