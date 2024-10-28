/* Create a function that returns a list [a, b], where 'a' is
  the largest of negative integers, and 'b' is the smallest
  of positive integers in a list.
  If there is no negative or positive integers, return them as null.
  Examples:
  largestSmallestIntegers([2, 4, 1, 3, 5, 7]) == [null, 1]
  largestSmallestIntegers([]) == [null, null]
  largestSmallestIntegers([0]) == [null, null]
  */
const largestSmallestIntegers = (lst) => {
  let smallest = null;
  let largest = null;

  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < 0 && (largest === null || lst[i] > largest)) {
      largest = lst[i];
    }
    if (lst[i] > 0 && (smallest === null || lst[i] < smallest)) {
      smallest = lst[i];
    }
  }

  return [largest, smallest];
};
