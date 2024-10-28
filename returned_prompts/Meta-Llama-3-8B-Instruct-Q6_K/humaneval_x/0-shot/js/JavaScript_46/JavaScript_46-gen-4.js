Here is a solution in JavaScript:

```javascript
const fib4 = (n) => {
  if (n <= 3) return 0;
  if (n === 4) return 2;
  const fib4s = [0, 0, 2, 0];
  for (let i = 4; i <= n; i++) {
    fib4s[i % 4] = fib4s[(i - 1) % 4] + fib4s[(i - 2) % 4] + fib4s[(i - 3) % 4] + fib4s[(i - 4) % 4];
  }
  return fib4s[n % 4];
};
```

The idea here is to use an array `fib4s` to store the values of the sequence. We initialize the array with the first four elements of the sequence. Then, we iterate from 4 to `n`, and for each `i`, we calculate the `i`th element of the sequence by adding the three previous elements (modulo 4 to handle the periodic nature of the sequence). Finally, we return the `n`th element of the sequence by indexing into the array with `n % 4`. This approach avoids the need for recursion and has a time complexity of O(n).