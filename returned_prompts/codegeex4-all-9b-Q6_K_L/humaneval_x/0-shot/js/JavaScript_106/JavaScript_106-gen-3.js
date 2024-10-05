Here is a solution in JavaScript:

```javascript
const f = (n) => {
  const result = [];
  for (let i = 1; i <= n; i++) {
    if (i % 2 === 0) {
      result.push(factorial(i));
    } else {
      result.push(sumTo(i));
    }
  }
  return result;
}

const factorial = (n) => {
  let result = 1;
  for (let i = 2; i <= n; i++) {
    result *= i;
  }
  return result;
}

const sumTo = (n) => {
  return (n * (n + 1)) / 2;
}
```

In this solution, the function `f` takes an integer `n` as input and returns an array of size `n`. The function loops over the range from 1 to `n` (inclusive), and for each index `i`, it checks if `i` is even or odd. If `i` is even, it calculates the factorial of `i` using the `factorial` function, and if `i` is odd, it calculates the sum of numbers from 1 to `i` using the `sumTo` function. The result is then pushed into the `result` array, which is returned at the end of the function.