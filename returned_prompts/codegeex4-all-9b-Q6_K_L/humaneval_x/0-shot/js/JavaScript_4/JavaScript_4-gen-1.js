The Mean Absolute Deviation (MAD) is a measure of variability or dispersion in a set of numbers. It's the average (mean) of the absolute differences between each number and the mean of the set.

Here's how you might implement `meanAbsoluteDeviation` in JavaScript:

```javascript
const meanAbsoluteDeviation = (numbers) => {
  const mean = numbers.reduce((a, b) => a + b, 0) / numbers.length;
  const deviations = numbers.map(n => Math.abs(n - mean));
  const mad = deviations.reduce((a, b) => a + b, 0) / deviations.length;
  return mad;
};
```

In this function:

1. We first calculate the mean of the numbers by summing all the numbers and dividing by their count.
2. Then, we calculate the absolute deviations from the mean for each number.
3. We find the mean of these absolute deviations to get the MAD.

Let's test this function with the given example:

```javascript
console.log(meanAbsoluteDeviation([1.0, 2.0, 3.0, 4.0])); // Should print 1.0
```

This function will return the Mean Absolute Deviation of the given numbers.