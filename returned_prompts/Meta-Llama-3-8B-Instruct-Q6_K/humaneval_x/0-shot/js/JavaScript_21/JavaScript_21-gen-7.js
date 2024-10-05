```javascript
const rescaleToUnit = (numbers) => {
  if (numbers.length < 2) {
    throw new Error('List must have at least two elements');
  }

  const min = Math.min(...numbers);
  const max = Math.max(...numbers);

  return numbers.map(num => (num - min) / (max - min));
};
```
This function first checks if the list has at least two elements. If not, it throws an error. Then it calculates the minimum and maximum values in the list using the spread operator `...` and the `Math.min` and `Math.max` functions. Finally, it uses the `map` method to apply the linear transformation to each element in the list, subtracting the minimum value and dividing by the range (max - min). This effectively scales the values to the range [0, 1].