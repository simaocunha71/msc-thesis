You can implement this function f using a for loop to iterate through the range from 1 to n, and an if-else statement to calculate the factorial or the sum based on the parity of the index i. Here is the JavaScript code:

```javascript
const f = (n) => {
  const result = [];
  for (let i = 1; i <= n; i++) {
    if (i % 2 === 0) {
      // calculate the factorial for even index
      result.push(factorial(i));
    } else {
      // calculate the sum for odd index
      result.push(sum(i));
    }
  }
  return result;
};

const factorial = (num) => {
  let result = 1;
  for (let i = 2; i <= num; i++) {
    result *= i;
  }
  return result;
};

const sum = (num) => {
  let result = 0;
  for (let i = 1; i <= num; i++) {
    result += i;
  }
  return result;
};
```

In this code, we define two helper functions factorial and sum to calculate the factorial and the sum of numbers from 1 to a given number. The function f uses these helper functions to calculate the values for even and odd indices and returns the resulting array.