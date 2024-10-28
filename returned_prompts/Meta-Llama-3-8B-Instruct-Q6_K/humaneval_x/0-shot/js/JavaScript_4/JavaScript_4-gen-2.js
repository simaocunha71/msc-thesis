```javascript
const meanAbsoluteDeviation = (numbers) => {
  const mean = numbers.reduce((a, b) => a + b, 0) / numbers.length;
  return numbers.map(x => Math.abs(x - mean)).reduce((a, b) => a + b, 0) / numbers.length;
};
```


Explanation:
The function calculates the Mean Absolute Deviation (MAD) for a given list of numbers. It first calculates the mean of the input numbers using the `reduce` method. Then it maps each number to its absolute difference from the mean using the `map` method, and calculates the sum of these absolute differences using the `reduce` method again. The result is the Mean Absolute Deviation. The time complexity is O(n), where n is the number of input numbers. The space complexity is O(1), as it only uses a constant amount of space.

Example usage:
```javascript
console.log(meanAbsoluteDeviation([1.0, 2.0, 3.0, 4.0])); // Output: 1.0
```


Note: This solution assumes that the input list is not empty. If the input list can be empty, you should add a check for that case and return a suitable value (e.g., `NaN` or `undefined`).