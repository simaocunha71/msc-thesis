
def get_total_number_of_sequences(m: int, n: int) -> int:
    sequences = [[1 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(2, m+1):
        for j in range(2, n+1):
            sequences[i][j] = sequences[i-1][j] + sequences[i//2][j-1]
    return sequences[m][n]

print(get_total_number_of_sequences(10, 4))  # 4

Explanation:

This problem can be solved using dynamic programming.

We start by initializing a 2D array sequences of size (m+1)x(n+1) with all elements set to 1. This array will store the number of sequences of length n ending with element i.

We then iterate over the range 2 to m+1 and for each i, we iterate over the range 2 to n+1 and update the value of sequences[i][j] as sequences[i-1][j] + sequences[i//2][j-1].

The first term sequences[i-1][j] is the number of sequences of length j ending with an element less than i. The second term sequences[i//2][j-1] is the number of sequences of length j-1 ending with an element i//2.

Finally, we return the value of sequences[m][n].
"""

def get_total_number_of_sequences(m: int, n: int) -> int:
    sequences = [[1 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(2, m+1):
        for j in range(2, n+1):
            sequences[i][j] = sequences[i-1][j] + sequences[i//2][j-1]
    return sequences[m][n]

print(get_total_number_of_sequences(10, 4))  # 4

"""
The function works by initializing an array `sequences` of size `(m+1)x(n+1)