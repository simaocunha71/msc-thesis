Here is a JavaScript solution for the problem:

```javascript
const roundedAvg = (n, m) => {
  if (n > m) {
    return -1;
  }
  let sum = 0;
  for (let i = n; i <= m; i++) {
    sum += i;
  }
  let avg = Math.round(sum / (m - n + 1));
  return avg.toString(2);
};
```

Here's an explanation of the code:

1. We first check if `n` is greater than `m`. If it is, we return -1 as per the problem statement.
2. We initialize a variable `sum` to 0, which will be used to store the sum of the integers from `n` to `m`.
3. We use a for loop to iterate from `n` to `m` (inclusive) and add each integer to `sum`.
4. We calculate the average by dividing `sum` by the number of integers (i.e., `m - n + 1`).
5. We use `Math.round` to round the average to the nearest integer.
6. Finally, we convert the rounded average to binary using the `toString` method with base 2, and return the result.