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
The function `sumToN` takes an integer `n` as an argument and returns the sum of all integers from 1 to `n`. It uses a `for` loop to iterate from 1 to `n`, adding each integer to a running total `sum`. Finally, it returns the total sum. This implementation is simple and efficient, with a time complexity of O(n).