Here is the implementation of the function f:
```javascript
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

1. We define a function f that takes an integer n as a parameter.
2. We initialize an empty array result to store the result.
3. We use a for loop to iterate from 1 to n.
4. For each iteration, we check if the current index i is even using the modulo operator (i % 2 === 0). If it is, we calculate the factorial of i using the factorial function and push it to the result array.
5. If i is odd, we calculate the sum of numbers from 1 to i using a nested for loop and push it to the result array.
6. Finally, we return the result array.

The factorial function is a separate function that calculates the factorial of a given number n. It uses a for loop to iterate from 2 to n and multiply the result by each number.

You can test the function f with different values of n, such as f(5) == [1, 2, 6, 24, 15].