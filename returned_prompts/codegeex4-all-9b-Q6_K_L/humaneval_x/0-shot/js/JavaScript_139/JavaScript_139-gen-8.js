To solve this problem, we need to calculate the factorial of a number and then multiply it by the factorial of the number minus one, and so on until we reach 1. Here's how you can do it using JavaScript:

```javascript
const specialFactorial = (n) => {
  let factorial = 1;
  let specialFactorial = 1;

  for(let i = n; i > 0; i--) {
    factorial *= i;
    specialFactorial *= factorial;
  }

  return specialFactorial;
}
```

In this code, we initialize two variables, `factorial` and `specialFactorial`, to 1. We then start a loop from `n` down to 1, multiplying `factorial` by the current number and `specialFactorial` by the current `factorial`. After the loop, we return `specialFactorial`, which is the result of the special factorial calculation.