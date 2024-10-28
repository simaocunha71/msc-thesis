Here is a simple recursive solution for the problem:

```javascript
const sumToN = (n) => {
  if (n === 1) {
    return 1;
  } else {
    return n + sumToN(n - 1);
  }
};
```

This function works by adding the current number `n` to the sum of all numbers from 1 to `n-1`. The base case for the recursion is when `n` is 1, in which case the function returns 1. 

Please note that this is not the most efficient solution for large values of `n`, as it does a lot of repeated work. A more efficient solution would be to use an iterative approach with a loop. Here is the iterative solution:

```javascript
const sumToN = (n) => {
  let sum = 0;
  for (let i = 1; i <= n; i++) {
    sum += i;
  }
  return sum;
};
```

This function works by initializing a variable `sum` to 0, then adding each number from 1 to `n` to `sum`. The final value of `sum` is returned. This solution is more efficient than the recursive solution for large values of `n`, as it does not do repeated work. 