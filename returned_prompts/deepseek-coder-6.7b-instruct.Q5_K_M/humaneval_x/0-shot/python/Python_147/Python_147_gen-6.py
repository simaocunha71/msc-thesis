
    def get_max_triples(n):
        count = 0
        a = [0]*n
        for i in range(1, n+1):
            a[i-1] = i*i - i + 1
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if (a[i] + a[j] + a[k]) % 3 == 0:
                        count += 1
        return count

    print(get_max_triples(5))  # Output: 1

Explanation:

In this problem, we are asked to create an array of length n where each element is calculated as i*i - i + 1, i ranging from 1 to n. Then, we need to count the number of triples (a[i], a[j], a[k]) where i < j < k such that the sum of the elements of the triple is a multiple of 3.

The algorithm used is a brute force approach. It iterates over all possible combinations of three elements in the array and checks if their sum is divisible by 3. It increments a counter each time it finds such a triple. Finally, it returns the count.

The time complexity of this algorithm is O(n^3) as there are n^3 combinations to check. This makes it inefficient for large values of n.

This algorithm is not efficient, it can be improved by using dynamic programming or other more efficient methods.

Note: This solution is correct but it's not optimal for large inputs. It's a brute force solution.
"""

# Dynamic Programming Solution

def get_max_triples(n):
    a = [i * i - i + 1 for i in range(1, n + 1)]
    dp = [[0] * 3 for _ in range(n)]
    count = 0

    for i in range(n):
        dp[i][a[i] % 3] += 1
        for j in range(3):
            if i > 0:
                dp[i][j] += dp[i - 1][j]
        if i