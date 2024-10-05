Here is the solution using a simple linear transformation:
```
const rescaleToUnit = (numbers) => {
  const min = Math.min(...numbers);
  const max = Math.max(...numbers);
  return numbers.map((num) => (num - min) / (max - min));
};
```
Explanation:

1. We first find the minimum and maximum values in the input array using the `Math.min` and `Math.max` functions with the spread operator (`...`) to pass the array as separate arguments.
2. We then use the `map` method to apply a transformation to each element in the array.
3. The transformation is a linear scaling, where each element is subtracted by the minimum value and then divided by the range (`max - min`). This has the effect of mapping the smallest value to 0 and the largest value to 1.
4. The resulting array is returned as the output.

Example:
```
const numbers = [1.0, 2.0, 3.0, 4.0, 5.0];
const result = rescaleToUnit(numbers);
console.log(result); // Output: [0.0, 0.25, 0.5, 0.75, 1.0]
``` 