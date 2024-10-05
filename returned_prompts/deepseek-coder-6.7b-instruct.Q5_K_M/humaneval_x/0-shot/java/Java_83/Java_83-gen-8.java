        if (n <= 0) {
            return 0;
        }

        if (n == 1) {
            return 1;
        }

        int[][] dp = new int[n][2];
        dp[0][0] = dp[0][1] = 1;

        for(int i = 1; i < n; i++) {
            dp[i][0] = dp[i-1][0] + dp[i-1][1];
            dp[i][1] = dp[i-1][0];
        }

        return 2*dp[n-1][0] - (n > 1 ? 1 : 0);
    }
}
```

Explanation:

This solution is using dynamic programming to solve the problem.

`dp[i][0]` means the count of the numbers of i-digit positive integers that start with 1.

`dp[i][1]` means the count of the numbers of i-digit positive integers that end with 1.

For `dp[i][0]`, it's the sum of `dp[i-1][0]` and `dp[i-1][1]` because we can add 0-9 to the front of a number that starts with 1 or ends with 1.

For `dp[i][1]`, it's `dp[i-1][0]` because we can add 0-9 to the end of a number that starts with 1.

Finally, the answer is 2*`dp[n-1][0]` - 1 if n > 1, otherwise 2*`dp[n-1][0]`. We subtract 1 because if n == 1, we don't count the number 1 itself.

This solution has a time complexity of O(n) and a space complexity of O(n).































































