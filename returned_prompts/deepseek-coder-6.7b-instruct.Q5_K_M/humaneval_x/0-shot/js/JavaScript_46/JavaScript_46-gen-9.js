  if (n < 2) {
    return 0;
  }
  if (n === 2) {
    return 2;
  }

  let a = 0;
  let b = 0;
  let c = 2;
  let d = 0;
  let e = 0;

  for (let i = 4; i <= n; i++) {
    e = a + b + c + d;
    a = b;
    b = c;
    c = d;
    d = e;
  }

  return e;
};

console.log(fib4(5)); // 4
console.log(fib4(6)); // 8
console.log(fib4(7)); // 14
```

### Solution Explanation:

The solution starts by initializing variables a, b, c, d, and e to 0, 0, 2, 0, 0. These are the initial four values of the sequence.

The loop starts at 4 because we've already initialized the first four values. The loop continues until it reaches the nth value we're interested in.

Inside the loop, the variable e is updated to the sum of the variables a, b, c, and d. Then the variables a, b, c, and d are updated to the values of b, c, d, and e respectively, so that they are ready for the next iteration.

Finally, the function returns the nth value of the sequence, which is stored in the variable e.

This solution uses a constant amount of memory and runs in linear time, so it's quite efficient.

Note that this code will not work correctly for negative values of n, because the Fibonacci sequence is not defined for negative indices. You might want to add some error checking for this.

Also, if you're planning to use this code in a real application, you should consider using a big integer library (like BigInteger.js) to handle very large numbers. The built-in JavaScript Number type can only safely represent integers up to Number.MAX_SAFE_INTEGER, which is about 9 quadrillion.

```javascript
```

```javascript

```

```javascript