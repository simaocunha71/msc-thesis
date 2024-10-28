/* Create a function that takes in an array of numbers and returns an array with only the odd numbers.
  Examples
  oddsOnly([]) ➞ []
  oddsOnly([1, 2, 3, 4, 5]) ➞ [1, 3, 5]
  oddsOnly([1, 2, 3, 4, 5, 6, 7, 8, 9]) ➞ [1, 3, 5, 7, 9]
  */
const oddsOnly = (arr) => {
  return arr.filter(function(item) {
    return item % 2 !== 0;
  });
}

