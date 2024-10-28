Here is the implementation in JavaScript:
```javascript
const meanAbsoluteDeviation = (numbers) => {
  const mean = numbers.reduce((acc, curr) => acc + curr, 0) / numbers.length;
  return numbers.map(x => Math.abs(x - mean)).reduce((acc, curr) => acc + curr, 0) / numbers.length;
};
```
Explanation:

1. Calculate the mean of the input numbers by summing them up and dividing by the length of the array.
2. Calculate the absolute differences between each number and the mean using the `map` method.
3. Calculate the sum of these absolute differences using the `reduce` method.
4. Divide the sum by the length of the array to get the Mean Absolute Deviation (MAD).

You can test this function with the example input `[1.0, 2.0, 3.0, 4.0]`:
```javascript
console.log(meanAbsoluteDeviation([1.0, 2.0, 3.0, 4.0])); // Output: 1.0
```
This implementation assumes that the input array is non-empty. If the input array is empty, the function will throw an error when trying to calculate the mean. You may want to add a check for this case and return a suitable value (e.g., `NaN` or a custom error message).