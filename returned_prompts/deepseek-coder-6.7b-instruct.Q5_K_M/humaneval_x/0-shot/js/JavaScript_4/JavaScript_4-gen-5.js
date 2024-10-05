  let mean = numbers.reduce((accum, curr) => accum + curr, 0) / numbers.length;
  let differences = numbers.map(num => Math.abs(num - mean));
  let mad = differences.reduce((accum, curr) => accum + curr, 0) / numbers.length;
  return mad;
};

console.log(meanAbsoluteDeviation([1.0, 2.0, 3.0, 4.0])); // Output: 1.0
```

Here is a JavaScript function that calculates the Mean Absolute Deviation (MAD) of a given array of numbers.

First, we calculate the mean of the numbers in the array by summing them all and dividing by the length of the array. This is done with the `reduce` method.

Next, we create a new array `differences` that contains the absolute differences between each number in the original array and the mean.

Finally, we calculate the mean of these differences to get the Mean Absolute Deviation (MAD).

This program will print `1.0` to the console.

```javascript
console.log(meanAbsoluteDeviation([1.0, 2.0, 3.0, 4.0])); // Output: 1.0
```

The function `meanAbsoluteDeviation` takes an array of numbers as an argument and returns the Mean Absolute Deviation of these numbers.

The `reduce` method is used to calculate the sum and mean of the numbers. The `map` method is used to create an array of the absolute differences between each number and the mean. The Mean Absolute Deviation is then calculated by taking the mean of these differences.

The function uses JavaScript's built-in `Math.abs` function to calculate the absolute difference between numbers, and the `reduce` method to sum these differences and the mean of the numbers.

The `console.log` function is used to print the result of the `meanAbsoluteDeviation` function to the console.

The `meanAbsoluteDeviation` function will return `1.0` for the input `[1.0, 2.0, 3.0, 4.0]