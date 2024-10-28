```javascript
const roundedAvg = (n, m) => {
  if (n > m) return -1;
  const sum = Array.from({ length: m - n + 1 }, (_, i) => n + i).reduce((a, b) => a + b, 0);
  const avg = Math.round(sum / (m - n + 1));
  return avg.toString(2);
};
```


Explanation:
- First, we check if `n` is greater than `m`. If it is, we return `-1` as per the problem statement.
- Then, we calculate the sum of the integers from `n` to `m` (inclusive) using `Array.from` to create an array of numbers from `n` to `m` and then using `reduce` to sum up the numbers.
- After that, we calculate the average by dividing the sum by the number of integers (`m - n + 1`).
- Finally, we round the average to the nearest integer using `Math.round` and convert the result to binary using `toString(2)` and return it.
- The binary string is prefixed with `'0b'` to indicate that it's a binary number.