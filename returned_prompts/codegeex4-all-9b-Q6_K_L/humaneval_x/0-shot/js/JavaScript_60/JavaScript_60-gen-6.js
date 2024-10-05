You can use a loop to add up the numbers from 1 to n. Here's how you can implement the `sumToN` function in JavaScript:

```javascript
const sumToN = (n) => {
  let sum = 0;
  for (let i = 1; i <= n; i++) {
    sum += i;
  }
  return sum;
}
```

This function initializes a variable `sum` to 0, then loops from 1 to n (inclusive), adding each number to `sum`. Finally, it returns the value of `sum`.