```
function isEqualToSumEven(n) {
  for (let a = 2; a <= n; a += 2) {
    for (let b = 2; b <= n; b += 2) {
      for (let c = 2; c <= n; c += 2) {
        for (let d = 2; d <= n; d += 2) {
          if (a + b + c + d === n) {
            return true;
          }
        }
      }
    }
  }
  return false;
}
```


This function iterates through all possible combinations of 4 even numbers, checks if their sum equals the given number, and returns `true` if it does, or `false` if it doesn't. This solution is not efficient for large numbers, as it has a time complexity of O(n^4). However, it works correctly for small inputs and provides a clear understanding of the problem. For larger inputs, a more efficient solution would be needed.

For example, you could use a dynamic programming approach to reduce the time complexity to O(n^2). Here's an example of how you could implement that:

```
function isEqualToSumEven(n) {
  let dp = new Array(n + 1).fill(false);
  dp[0] = true;
  for (let i = 2; i <= n; i += 2) {
    dp[i] = true;
    for (let j = i; j <= n; j += 2) {
      dp[j] += dp[j - i];
    }
  }
  for (let i = 2; i <= n; i += 2) {
    for (let j = 2; j <= n; j += 2) {
      if (dp[n - i - j]) {
        return true;
      }
    }
  }
  return false;
}
```

This function uses dynamic programming to build up a table of whether each number can be written as the sum of 4 even numbers. It then checks the table to see if the given number can be written as the sum of exactly 4 positive even numbers. This solution is much more efficient for large inputs.