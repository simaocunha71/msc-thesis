/* Given list of numbers (of at least two elements), apply a linear transform to that list,
  such that the smallest number will become 0 and the largest will become 1
  >>> rescaleToUnit([1.0, 2.0, 3.0, 4.0, 5.0])
  [0.0, 0.25, 0.5, 0.75, 1.0]
  */
const rescaleToUnit = (numbers) => {
  const min = Math.min(...numbers);
  const max = Math.max(...numbers);
  return numbers.map(n => (n - min) / (max - min));
}
