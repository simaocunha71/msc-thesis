```javascript
const sumToN = (n) => {
  let sum = 0;
  for (let i = 1; i <= n; i++) {
    sum += i;
  }
  return sum;
};
```


Explanation:

The function `sumToN` takes an integer `n` as input and returns the sum of all numbers from 1 to `n`. It uses a `for` loop to iterate from 1 to `n`, adding each number to a running total `sum`. The final value of `sum` is returned as the result. This is a simple and efficient implementation of the formula for the sum of an arithmetic series.