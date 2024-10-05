Here is a JavaScript solution that checks whether a given number `n` can be written as the sum of exactly 4 positive even numbers:
```javascript
const isEqualToSumEven = (n) => {
  for (let i = 2; i <= n; i += 2) {
    for (let j = 2; j <= n; j += 2) {
      for (let k = 2; k <= n; k += 2) {
        for (let l = 2; l <= n; l += 2) {
          if (i + j + k + l === n) {
            return true;
          }
        }
      }
    }
  }
  return false;
};
```
Here's an explanation of the code:

1. We start by initializing a variable `i` to 2, which is the smallest positive even number.
2. We then enter a loop that runs until `i` is greater than or equal to `n`.
3. Inside the loop, we start a new loop that runs until `j` is greater than or equal to `n`. We also initialize `j` to 2, which is the smallest positive even number.
4. We then enter a new loop that runs until `k` is greater than or equal to `n`. We also initialize `k` to 2, which is the smallest positive even number.
5. Inside the innermost loop, we start a new loop that runs until `l` is greater than or equal to `n`. We also initialize `l` to 2, which is the smallest positive even number.
6. We then check if the sum of `i`, `j`, `k`, and `l` is equal to `n`. If it is, we return `true`, indicating that `n` can be written as the sum of exactly 4 positive even numbers.
7. If we reach the end of the loops without finding a solution, we return `false`, indicating that `n` cannot be written as the sum of exactly 4 positive even numbers.

You can test this function with different inputs to see if it works correctly. For example, `isEqualToSumEven(8)` should return `true`, while `isEqualToSumEven(6)` should return `false`.