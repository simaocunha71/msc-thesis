/* Create a function that takes an array of numbers and returns the sum of all elements.
  Examples
  sumArray([1, 2, 3]) ➞ 6
  sumArray([-1, 2, 3]) ➞ 4
  sumArray([]) ➞ 0
  */
  const sumArray = arr => arr.reduce((a, b) => a + b, 0);

