  if (n < 1) return 0;
  if (n === 1) return 2;
  if (n === 2) return 4;

  let count = 0;
  let dp = Array(n + 1).fill(0);
  dp[1] = 2;
  dp[2] = 4;

  for (let i = 3; i <= n; i++) {
    dp[i] = 2 * dp[i - 1] + Math.pow(2, i - 2);
  }

  return dp[n];
};

console.log(startsOneEnds(2)); // 4
console.log(startsOneEnds(3)); // 10
console.log(startsOneEnds(4)); // 24
console.log(startsOneEnds(5)); // 56
```

### Solution:

This problem can be solved using dynamic programming. The idea is to use an array dp of size n+1 to store the count of n-digit numbers that start or end with 1.

We initialize dp[1] = 2 and dp[2] = 4 because there are 2 one-digit numbers (1, 1) and 4 two-digit numbers (11, 10, 01, 10) that start or end with 1.

Then for each i from 3 to n (inclusive), we calculate dp[i] as 2 * dp[i - 1] + Math.pow(2, i - 2) because for each i-digit number that starts or ends with 1, we can either have the first digit as 1 or the last digit as 1. The number of i-digit numbers that start with 1 is dp[i - 1] and the number of i-digit numbers that end with 1 is also dp[i - 1]. The number of i-digit numbers that start or end with 1 is the sum of these two, which is 2 * dp[i - 1]. Moreover, we can have i-digit numbers that start or end with 1 by appending 1 to the