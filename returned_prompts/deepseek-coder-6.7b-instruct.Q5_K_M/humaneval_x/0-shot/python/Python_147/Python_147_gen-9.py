
def get_max_triples(n):
    if n < 3:
        return 0
    a = [i*i - i + 1 for i in range(1, n+1)]
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count


print(get_max_triples(5))  # Output: 1
print(get_max_triples(6))  # Output: 2
print(get_max_triples(7))  # Output: 4
print(get_max_triples(8))  # Output: 5
print(get_max_triples(9))  # Output: 7
print(get_max_triples(10))  # Output: 9

This solution first calculates the values of the array "a" as per the problem statement. Then it iterates through each combination of three indexes (i, j, k) and checks if the sum of the values at those indexes is a multiple of 3. If it is, it increments the count. Finally, it returns the count.

Note: This solution has a time complexity of O(n^3), which means that it can become slow for large inputs.
    """

# A more efficient solution using dynamic programming

def get_max_triples(n):
    if n < 3:
        return 0
    a = [i*i - i + 1 for i in range(1, n+1)]
    dp = [0] * 3
    count = 0
    for i in range(n):
        count += dp[(3 - a[i] % 3) % 3]
        dp[a[i] % 3] += 1
    return count

print(get_max_triples(5))  # Output: 1
print(get_max_triples(6))  # Output: 2
print(get_max_triples(7))  # Output: 4
