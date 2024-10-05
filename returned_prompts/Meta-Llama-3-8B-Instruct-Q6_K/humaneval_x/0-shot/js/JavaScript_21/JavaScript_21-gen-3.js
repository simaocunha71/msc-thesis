```javascript
const rescaleToUnit = (numbers) => {
  const min = Math.min(...numbers);
  const max = Math.max(...numbers);
  return numbers.map(x => (x - min) / (max - min));
};
```


Explanation:

1. We first find the minimum and maximum values in the input list using the `Math.min` and `Math.max` functions with the spread operator (`...numbers`).

2. Then, we use the `map` method to transform each element in the list. For each element `x`, we subtract the minimum value from it, and then divide the result by the difference between the maximum and minimum values. This effectively maps the smallest value to 0 and the largest value to 1.

3. The transformed list is then returned.

Example usage:
```javascript
console.log(rescaleToUnit([1.0, 2.0, 3.0, 4.0, 5.0]));
// Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```


This function will work for any list of numbers, not just those with exactly two elements. It will also work correctly if the list contains duplicate values, as it uses the minimum and maximum values to determine the transformation.