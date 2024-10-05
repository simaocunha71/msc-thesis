Here is a solution using JavaScript:

```javascript
const f = (n) => {
  let result = [];

  for (let i = 1; i <= n; i++) {
    if (i % 2 === 0) {
      result.push(factorial(i));
    } else {
      result.push(sum(i));
    }
  }

  return result;
};

const factorial = (n) => {
  let result = 1;
  for (let i = 1; i <= n; i++) {
    result *= i;
  }
  return result;
};

const sum = (n) => {
  let result = 0;
  for (let i = 1; i <= n; i++) {
    result += i;
  }
  return result;
};
```

In this solution, the `f` function loops from 1 to `n` and for each index `i`, it checks if `i` is even or odd. If `i` is even, it calculates the factorial of `i` using the `factorial` function and pushes the result into the `result` array. If `i` is odd, it calculates the sum of numbers from 1 to `i` using the `sum` function and pushes the result into the `result` array. Finally, it returns the `result` array.

The `factorial` function calculates the factorial of a number by multiplying the numbers from 1 to the number.

The `sum` function calculates the sum of numbers from 1 to a number by adding the numbers from 1 to the number.