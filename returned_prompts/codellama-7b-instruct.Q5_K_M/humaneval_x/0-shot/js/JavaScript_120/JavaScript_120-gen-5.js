/*
  Given an array arr of integers, find the maximum value in the array.

  Example 1:

      Input: arr = [1, 2, 3, 4, 5, 6]
      Output: 6

  Example 2:

      Input: arr = [-1, -2, -3, -4, -5, -6]
      Output: -1

  Example 3:

      Input: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
      Output: 10

  Note:
      1. The length of the array will be in the range of [1, 1000].
      2. The number could be negative.
  */
const maximum = (arr) => {
  let max = -Infinity;
  arr.forEach(number => {
    if (number > max) {
      max = number;
    }
  });
  return max;
}

