/* For a given list of input numbers, calculate Mean Absolute Deviation
  around the mean of this dataset.
  Mean Absolute Deviation is the average absolute difference between each
  element and a centerpoint (mean in this case):
  MAD = average | x - x_mean |
  >>> meanAbsoluteDeviation([1.0, 2.0, 3.0, 4.0])
  1.0
  */
const meanAbsoluteDeviation = (numbers) => {
  const mean = numbers.reduce((a, b) => a + b, 0) / numbers.length
  return numbers.reduce((a, b) => a + Math.abs(b - mean), 0) / numbers.length
}

