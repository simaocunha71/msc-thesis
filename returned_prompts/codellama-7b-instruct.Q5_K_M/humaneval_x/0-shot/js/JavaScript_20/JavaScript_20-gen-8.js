/* From a supplied list of numbers (of length at least two) select and return two that are the closest to each
  other and return them in order (smaller number, larger number).
  >>> findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
  (2.0, 2.2)
  >>> findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
  (2.0, 2.0)
  */
const findClosestElements = (numbers) => {

  let smallestDifference = Infinity;
  let closestPair = [];

  for (let i = 0; i < numbers.length - 1; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      const difference = Math.abs(numbers[i] - numbers[j]);
      if (difference < smallestDifference) {
        closestPair = [numbers[i], numbers[j]];
        smallestDifference = difference;
      }
    }
  }

  return closestPair;
}
