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
  let m = 0,
      ma = 0;
  for(let i=0 ; i<n ; i++) ma += Math.abs(numbers[i] - (m + ma/n));
  return ma/(n-1);
};
