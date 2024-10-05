```js
  let total = 1;
  for (let i = 1; i <= n; i++) {
    total *= factorial(i);
  }
  return total;
};

const factorial = (n) => {
  if (n === 0) return 1;
  return n * factorial(n - 1);
};
```

I have created two functions. The `factorial` function calculates the factorial of a number, and the `specialFactorial` function calculates the special factorial of a number by multiplying the factorials of all numbers from 1 to the input number.