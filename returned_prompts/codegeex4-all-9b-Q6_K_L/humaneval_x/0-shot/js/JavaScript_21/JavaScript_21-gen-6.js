Here's how you can write this function in JavaScript:

```javascript
const rescaleToUnit = (numbers) => {
  const min = Math.min(...numbers);
  const max = Math.max(...numbers);
  return numbers.map(n => (n - min) / (max - min));
};
```

This function works by first finding the minimum and maximum values in the list, then scaling all the numbers in the list so that the minimum value becomes 0 and the maximum value becomes 1. The `map` function is used to apply this transformation to each number in the list, and the results are returned as a new list.