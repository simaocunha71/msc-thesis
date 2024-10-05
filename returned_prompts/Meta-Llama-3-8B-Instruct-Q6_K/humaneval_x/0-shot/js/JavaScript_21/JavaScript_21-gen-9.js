```javascript
const rescaleToUnit = (numbers) => {
  const min = Math.min(...numbers);
  const max = Math.max(...numbers);
  return numbers.map(num => (num - min) / (max - min));
};
```
Explanation:
- We first find the minimum and maximum values in the input array using the `Math.min` and `Math.max` functions with the spread operator (`...numbers`).
- Then, we use the `map` method to apply the linear transform to each element in the array. For each element `num`, we subtract the minimum value `min` and then divide the result by the range `max - min`. This effectively scales the values to the unit interval [0, 1].
- The resulting array is returned as the output.