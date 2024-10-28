```javascript
const rescaleToUnit = (numbers) => {
  const min = Math.min(...numbers);
  const max = Math.max(...numbers);
  return numbers.map(x => (x - min) / (max - min));
};
```
Explanation:

1. First, we find the minimum and maximum values in the input list using `Math.min` and `Math.max` with the spread operator (`...numbers`).
2. Then, we create a new list where each element is mapped to a new value using the formula `(x - min) / (max - min)`. This formula shifts the range of values so that the smallest value becomes 0 and the largest becomes 1.
3. The `map` method is used to apply this transformation to each element in the original list.
4. The resulting list is returned as the output.

Example usage:
```javascript
console.log(rescaleToUnit([1.0, 2.0, 3.0, 4.0, 5.0]));
// Output: [0, 0.25, 0.5, 0.75, 1]
``` 