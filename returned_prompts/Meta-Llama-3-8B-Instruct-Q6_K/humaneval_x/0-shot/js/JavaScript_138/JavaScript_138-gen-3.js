```javascript
const isEqualToSumEven = (n) => {
  for (let i = 2; i <= n; i += 2) {
    let sum = 0;
    for (let j = 2; j <= n; j += 2) {
      if (i + j <= n) {
        sum += i + j;
        if (sum === n) return true;
      } else break;
    }
  }
  return false;
};
```



Explanation:

The function `isEqualToSumEven` takes an integer `n` as input and checks whether it can be written as the sum of exactly 4 positive even numbers.

The function uses two nested loops to iterate over all even numbers from 2 to `n`. The outer loop iterates over the first even number, `i`, and the inner loop iterates over the second even number, `j`. The sum of `i` and `j` is calculated and added to the `sum` variable. If the sum reaches `n`, the function returns `true`.

If the sum does not reach `n` after iterating over all even numbers, the function returns `false`.

The function is implemented in a way that it only checks for even numbers and does not consider odd numbers. This is because the problem statement specifies that the numbers should be even.