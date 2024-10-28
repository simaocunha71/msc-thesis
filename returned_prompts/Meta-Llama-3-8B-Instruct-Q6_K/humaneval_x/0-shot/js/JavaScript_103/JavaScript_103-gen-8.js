Here is the solution in JavaScript:
```
const roundedAvg = (n, m) => {
  if (n > m) return -1;

  const sum = Array.from({ length: m - n + 1 }, (_, i) => n + i).reduce((acc, curr) => acc + curr, 0);
  const avg = Math.round(sum / (m - n + 1));

  return avg.toString(2);
};
```
Here's an explanation of the code:

1. We first check if `n` is greater than `m`. If it is, we return `-1` according to the problem statement.
2. We create an array of integers from `n` to `m` using `Array.from` and `reduce` to calculate the sum of these integers.
3. We calculate the average by dividing the sum by the number of integers (`m - n + 1`).
4. We round the average to the nearest integer using