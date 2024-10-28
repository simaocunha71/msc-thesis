The problem can be solved by using dynamic programming. We can create an array of size `n+1` where `dp[i]` represents the `i-th` element of the fib4 number sequence. We initialize the base cases `dp[0]`, `dp[1]`, `dp[2]`, and `dp[3]` as 0, 0, 2, and 0 respectively. Then we calculate the rest of the elements by using the formula `dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]`. Finally, we return `dp[n]` as the result.

Here is the Java code for the problem:
```java
public int fib4(int n) {
    int[] dp = new int[n+1];
    dp[0] = 0;
    dp[1] = 0;
    dp[2] = 2;
    dp[3] = 0;
    for (int i = 4; i <= n; i++) {
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4];
    }
    return dp[n];
}
```
This solution has a time complexity of O(n) and a space complexity of O(n). It is efficient and easy to understand. It can be used to compute the `n-th` element of the fib4 number sequence for any positive integer `n`.