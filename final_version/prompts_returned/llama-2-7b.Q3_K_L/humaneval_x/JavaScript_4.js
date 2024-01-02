/* For a given list of input numbers, calculate Mean Absolute Deviation
  around the mean of this dataset.
  Mean Absolute Deviation is the average absolute difference between each
  element and a centerpoint (mean in this case):
  MAD = average | x - x_mean |
  >>> meanAbsoluteDeviation([1.0, 2.0, 3.0, 4.0])
  1.0
  */
const meanAbsoluteDeviation = (numbers) => {
  const n = numbers.length;
  let sum = 0;
  numbers.forEach((number) => {
    sum += Math.abs(number - number / n); // Sum all the absolute differences.
  });
  return sum / n; // Divide by the number of elements to get the MAD.
};
