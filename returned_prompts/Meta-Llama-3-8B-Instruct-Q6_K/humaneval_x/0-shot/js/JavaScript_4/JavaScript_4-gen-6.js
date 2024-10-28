```
function meanAbsoluteDeviation(numbers) {
  const mean = numbers.reduce((a, b) => a + b, 0) / numbers.length;
  return numbers.map(x => Math.abs(x - mean)).reduce((a, b) => a + b, 0) / numbers.length;
}
```


Explanation:
1. First, we calculate the mean of the input numbers by summing up all the numbers and dividing by the length of the array.
2. Then, we calculate the absolute difference between each number and the mean.
3. We sum up these absolute differences to get the total sum of absolute deviations.
4. Finally, we divide the total sum by the length of the array to get the Mean Absolute Deviation.

Example:
```
console.log(meanAbsoluteDeviation([1.0, 2.0, 3.0, 4.0]));  // Output: 1
```
Note: The meanAbsoluteDeviation function assumes that the input is a non-empty array of numbers. If the input array is empty, the function will throw an error. You might want to add error handling to make the function more robust.