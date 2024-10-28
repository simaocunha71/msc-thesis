/* From a list of integers, remove all elements that occur more than once.
  Keep order of elements left the same as in the input.
  >>> removeDuplicates([1, 2, 3, 2, 4])
  [1, 3, 4]
  */
const removeDuplicates = (numbers) => {
  const seen = new Set();
  const result = [];

  for (let i = 0; i < numbers.length; i++) {
    if (!seen.has(numbers[i])) {
      seen.add(numbers[i]);
      result.push(numbers[i]);
    }
  }

  return result;
}