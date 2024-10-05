To solve this problem, we need to calculate the factorial of each number from 1 to n and then multiply all these factorials together. Here's the code to solve the problem:

```javascript
const specialFactorial = (n) => {
  let result = 1;
  for (let i = 1; i <= n; i++) {
    let factorial = 1;
    for (let j = 1; j <= i; j++) {
      factorial *= j;
    }
    result *= factorial;
  }
  return result;
};
```

The function `specialFactorial` takes an integer `n` as input and initializes a variable `result` to 1. It then iterates over the numbers from 1 to n using a for loop. For each number `i`, it calculates the factorial of `i` using another for loop and multiplies it with the current value of `result`. Finally, it returns the final value of `result`.