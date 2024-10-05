Here is a JavaScript solution for the problem:
```
const f = (n) => {
  const result = [];
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
Here's an explanation of the code:

The `f` function takes an integer `n` as input and returns a list of size `n`. It uses a for loop to iterate from 1 to `n`.

Inside the loop, it checks if the current number `i` is even (i.e., `i % 2 === 0`). If it is, it calculates the factorial of `i` using the `factorial` function and pushes it to the result list.

If `i` is odd, it calculates the sum of numbers from 1 to `i` using a nested for loop and pushes the sum to the result list.

Finally, the `f` function returns the result list.

The `factorial` function is a helper function that calculates the factorial of a given number `n` using a for loop.

You can test the `f` function with different inputs, such as `f(5)` or `f(10)`, to see the expected output. For example, `f(5)` should return `[1, 2, 6, 24, 15]`.