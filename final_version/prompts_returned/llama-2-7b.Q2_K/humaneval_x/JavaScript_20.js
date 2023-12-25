/* From a supplied list of numbers (of length at least two) select and return two that are the closest to each
  other and return them in order (smaller number, larger number).
  >>> findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
  (2.0, 2.2)
  >>> findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
  (2.0, 2.0)
  */
const findClosestElements = (numbers) => {
  const size = numbers.length;
  if (!size) return 'Empty array';

  // Sort our list of numbers in the order of smallest to largest,
  // so that we can perform comparisons later on and get the same results as
  // if all of them were already the correct order from the beginning.
  const sortedNumbers = [...numbers].sort((a, b) => a - b);
  // Since each element is smaller than every other element,
  // use it to find the index in which the first two elements that are closest to each other appear.
  const result = sortedNumbers[0] < sortedNumbers[1] ? [sortedNumbers[0], sortedNumbers[1]] : [sortedNumbers[1], sortedNumbers[0]];
  return result;
};
