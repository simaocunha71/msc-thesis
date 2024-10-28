/*
  Given an array of non-negative integers, return a copy of the given array after sorting,
  you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
  or sort it in descending order if the sum( first index value, last index value) is even.

  Note:
  * don't change the given array.

  Examples:
  * sortArray([]) => []
  * sortArray([5]) => [5]
  * sortArray([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
  * sortArray([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
  */
const sortArray = (array) => {
  const sum = (array[0] + array[array.length - 1]);
  const sorted = array.sort((a, b) => {
    if (sum % 2 === 0) {
      return b - a;
    }
    return a - b;
  });
  return sorted;
};
