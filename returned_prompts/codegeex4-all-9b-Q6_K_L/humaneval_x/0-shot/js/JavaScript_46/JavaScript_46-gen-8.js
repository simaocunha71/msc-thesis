```javascript
const fib4 = (n) => {
  if (n === 0 || n === 1) return 0;
  if (n === 2) return 2;

  let a = 0, b = 0, c = 2, d = 0, result = 0;

  for (let i = 3; i <= n; i++) {
    result = a + b + c + d;
    a = b;
    b = c;
    c = d;
    d = result;
  }

  return result;
}
```

Explanation:
We use a loop to calculate the fib4 number sequence. We keep track of the last four numbers in the sequence and update them in each iteration of the loop. The result is the sum of the last four numbers. The initial values are set based on the definition of the fib4 number sequence.