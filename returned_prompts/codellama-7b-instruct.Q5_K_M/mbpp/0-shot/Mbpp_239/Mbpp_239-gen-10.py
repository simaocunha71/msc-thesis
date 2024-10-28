"""
We want to count the number of sequences that can be formed with length n and elements in the range [2, m].

The number of sequences with length n and elements in the range [2, m] is the number of sequences with length n-1 and elements in the range [3, m] + the number of sequences with length n-1 and elements in the range [2, m-1].

We can write a recursive formula:
T(n, m) = T(n-1, m) + T(n-1, m-1)

We can also write this as a loop:
T(n, m) = 1 + sum(T(n-1, i) for i in range(2, m))

We can memoize the function to avoid re-computing the same sub-problems.

We can also optimize it by using a dynamic programming approach:
"""

# Time complexity: O(n*m)
# Space complexity: O(n*m)

def get_total_number_of_sequences(m, n):
    memo = {}

    def T(n, m):
        if n == 0:
            return 1
        if (n, m) in memo:
            return memo[(n, m)]
        total = 0
        for i in range(2, m+1):
            total += T(n-1, i)
        memo[(n, m)] = total
        return total

    return T(n, m)


"""
Alternative recursive solution:

def get_total_number_of_sequences(m, n):
    if n == 0:
        return 1
    total = 0
    for i in range(2, m+1):
        total += get_total_number_of_sequences(m, n-1)
    return total
"""
