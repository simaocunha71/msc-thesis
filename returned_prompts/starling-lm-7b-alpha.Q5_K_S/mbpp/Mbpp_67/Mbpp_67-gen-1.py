def bell_number(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        dp = [0]* (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = sum(dp[0:i])
        return dp[n]

"""
The Bell number B(n) counts the number of ways to partition a set with n elements.
For example, B(3) = 5, since there are five different ways to partition the set {1, 2, 3}: {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, and {1, 2, 3}.

To solve this problem, you can use the following steps:

1. Create a dynamic programming table dp[0..n] to store the number of partitions for each set size from 0 to n. Initialize all values to 0.

2. Set the first two values of dp to 1, since there is only one way to partition a set with 0 or 1 element.

3. For each set size i from 2 to n, calculate the number of partitions by summing all previous partitions (from 0 to i). This is because each element of the set can either be in the partition or not, resulting in 2^i partitions. However, this overcounts the number of partitions by a factor of 2, so we need to divide by 2 to get the correct count.

4. Finally, return the value at index n in the dp table, which represents the number of ways to partition a set with n elements.

The time complexity of this solution is O(n), since we are only performing a constant amount of work for each value of n. The space complexity is also O(n), since we need to store the dp table of size n+1.

For example, if we call the function bell_number(2), it will return 2, since there are two ways to partition the set {1, 2, 3}: {1}, {2}, {3}, {1, 2}, {