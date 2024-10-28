```javascript
const fib4 = (n) => {
  if (n < 0) {
    throw new Error('n must be a non-negative integer');
  }
  if (n === 0) {
    return 0;
  }
  if (n === 1) {
    return 0;
  }
  if (n === 2) {
    return 2;
  }
  const fib4Table = [0, 0, 2, 0];
  for (let i = 4; i <= n; i++) {
    fib4Table[i % 4] = (fib4Table[(i - 1) % 4] + fib4Table[(i - 2) % 4] + fib4Table[(i - 3) % 4] + fib4Table[(i - 4) % 4]);
  }
  return fib4Table[n % 4];
};
```


The function first checks if n is less than 0, and if so, throws an error. Then it checks if n is 0, 1, or 2, and returns the appropriate value.

Next, it initializes an array `fib4Table` with the first four values of the sequence: 0, 0, 2, and 0.

The function then uses a loop to compute the remaining values of the sequence, using the formula `fib4Table[i % 4] = (fib4Table[(i - 1) % 4] + fib4Table[(i - 2) % 4] + fib4Table[(i - 3) % 4] + fib4Table[(i - 4) % 4])`.

Finally, the function returns the nth value of the sequence, which is stored in `fib4Table[n % 4]`. This is because the sequence has a period of 4, so the nth value is the same as the (n % 4)th value. This trick reduces the number of calculations needed to compute the nth value from O(n) to O(1).