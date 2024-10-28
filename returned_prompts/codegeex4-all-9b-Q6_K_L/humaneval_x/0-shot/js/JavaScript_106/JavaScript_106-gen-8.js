Here is a possible solution in JavaScript:

```javascript
const f = (n) => {
  let result = [];
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
  for (let i = 1; i <= n; i++) {
    result *= i;
  }
  return result;
}

const sumTo = (n) => {
  let result = 0;
  for (let i = 1; i <= n; i++) {
    result += i;
  }
  return result;
}
```

In this solution, we use two helper functions: `factorial` and `sumTo`. The `factorial` function calculates the factorial of a given number, while the `sumTo` function calculates the sum of numbers from 1 to a given number. We iterate over the range from 1 to n, and for each index i, we check if it is even or odd. If it is even, we calculate the factorial of i and push it to the result array. If it is odd, we calculate the sum of numbers from 1 to i and push it to the result array. Finally, we return the result array.