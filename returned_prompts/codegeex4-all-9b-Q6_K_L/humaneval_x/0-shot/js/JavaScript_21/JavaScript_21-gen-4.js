```javascript
const rescaleToUnit = (numbers) => {
  let min = Math.min(...numbers);
  let max = Math.max(...numbers);
  return numbers.map(n => (n - min) / (max - min));
}
```

This solution works by first finding the minimum and maximum values in the list of numbers. Then it uses the map function to create a new list where each number is rescaled by subtracting the minimum value and then dividing by the range (max - min). This will ensure that the smallest number becomes 0 and the largest becomes 1.