```javascript
const meanAbsoluteDeviation = (numbers) => {
  const mean = numbers.reduce((acc, current) => acc + current, 0) / numbers.length;
  return numbers.reduce((acc, current) => acc + Math.abs(current - mean), 0) / numbers.length;
};
```


Here is how it works:

1. Calculate the mean of the input numbers. This is done by summing all the numbers and then dividing by the count of numbers.
2. Calculate the absolute difference between each number and the mean. This is done by subtracting the mean from each number and then taking the absolute value of the result.
3. Calculate the mean of these absolute differences. This is done by summing all the absolute differences and then dividing by the count of numbers.

The result is the Mean Absolute Deviation (MAD) of the input numbers.