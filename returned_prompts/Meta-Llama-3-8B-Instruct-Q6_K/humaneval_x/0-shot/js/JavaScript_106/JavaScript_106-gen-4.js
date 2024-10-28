Here is the JavaScript code that implements the function `f` as described:

```javascript
const f = (n) => {
  let result = [];
  for (let i = 1; i <= n; i++) {
    if (i % 2 === 0) {
      result.push(factorial(i));
    } else {
      let sum = 0;
      for (let j = 1; j <= i; j++) {
        sum += j;
      }
      result.push(sum);
    }
  }
  return result;
};

const factorial = (n) => {
  let result = 1;
  for (let i = 2; i <= n; i++) {
    result *= i;
  }
  return result;
};
```

In the above code, we define the function `f` which takes an integer `n` as an argument. It initializes an empty array `result` to store the result. It then iterates from 1 to `n` using a for loop. For each iteration, it checks if the current number `i` is even. If it is, it calculates the factorial of `i` using the `factorial` function and pushes it to the `result` array. If `i` is odd, it calculates the sum of numbers from 1 to `i` using another for loop and pushes it to the `result` array. Finally, it returns the `result` array.

The `factorial` function calculates the factorial of a given number `n` using a for loop. It initializes a variable `result` to 1 and then multiplies it by each number from 2 to `n`. It returns the final result.

You can test the function `f` with different values of `n` to see the output. For example, `f(5)` will return `[1, 2, 6, 24, 15]`.